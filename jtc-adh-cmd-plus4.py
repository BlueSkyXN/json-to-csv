import ijson
import pandas as pd
import argparse
import os

# 创建参数解析器
parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input JSON file')
# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv"), required=False, help='Path to output CSV file')
# 添加 chunk_size 参数
parser.add_argument('-s', '--chunksize', type=int, default=1000, required=False, help='Number of lines to read at a time')

args = parser.parse_args()

# 将数据逐行读取并转换为DataFrame
data = []
with open(args.input, 'r') as f:
    objects = ijson.items(f, 'item')
    for row in objects:
        data.append(row)
        if len(data) == args.chunksize:
            df = pd.DataFrame(data)
            abs_output_path = os.path.abspath(args.output)
            df.to_csv(abs_output_path, mode='a', header=not os.path.exists(abs_output_path), index=False)
            data = []
if data:
    df = pd.DataFrame(data)
    abs_output_path = os.path.abspath(args.output)
    df.to_csv(abs_output_path, mode='a', header=not os.path.exists(abs_output_path), index=False)

print(f'Successfully converted {args.input} to {os.path.abspath(args.output)}')
