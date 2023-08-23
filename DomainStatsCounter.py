import pandas as pd
import argparse
from collections import Counter

def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield [first] + list(iter(iterator, size))

def main(input_file, output_file, chunksize):
    # 创建一个Counter对象来存储整个文件的统计
    total_counts = Counter()

    with open(input_file, 'r') as file:
        # 获取列名
        columns = file.readline().strip().split(',')
        
        # 逐块读取文件
        for chunk in chunks(file, chunksize):
            # 将每个块转换为DataFrame
            df = pd.DataFrame([line.strip().split(',') for line in chunk], columns=columns)
            
            # 统计"QH"列中域名的出现次数
            total_counts.update(Counter(df['QH']))
    
    # 将结果转换为DataFrame
    result_df = pd.DataFrame.from_dict(total_counts, orient='index').reset_index()
    result_df.columns = ['Domain', 'Count']
    
    # 按计数降序排列
    result_df = result_df.sort_values(by='Count', ascending=False)

    # 保存结果到新的CSV文件
    result_df.to_csv(output_file, index=False)

    print(f"域名统计已保存到 {output_file}")

# 命令行参数解析
parser = argparse.ArgumentParser(description='统计域名出现次数')
parser.add_argument('-i', '--input', type=str, required=True, help='Path to input CSV file')
parser.add_argument('-o', '--output', type=str, required=True, help='Path to output CSV file')
parser.add_argument('-s', '--chunksize', type=int, default=100000, help='Number of lines to process at a time')
args = parser.parse_args()

main(args.input, args.output, args.chunksize)
