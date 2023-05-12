import argparse
import pandas as pd
import os
from tqdm import tqdm

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='Convert JSON query log to CSV format')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json") ,required=False, help='Path to input JSON file')

# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv") ,required=False, help='Path to output CSV file')

# 解析命令行参数
args = parser.parse_args()
print(args.input, args.output)

# 获取输入文件大小
input_file_size = os.path.getsize(args.input)

# 逐行读取JSON文件并转换为CSV格式
with open(args.input, 'r') as f:
    # 逐行读取JSON文件并处理
    lines = f.readlines()
    json_content = '[{}]'.format(','.join([line.strip() for line in lines]))

# 将JSON转换成DataFrame对象
df = pd.read_json(json_content)

# 在循环中逐行读取数据并添加到DataFrame中
for _, row in tqdm(df.iterrows(), total=len(df), desc="Converting"):
    pass

# 将数据保存为CSV文件
abs_output_path = os.path.abspath(args.output)
df.to_csv(abs_output_path, index=False)

# 打印输出路径
print(f"\n已将JSON数据成功转换并保存到文件：{abs_output_path}")
