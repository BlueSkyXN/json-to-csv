import pandas as pd
import json
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='Convert JSON data to CSV format')
parser.add_argument('-i', '--input', type=str, required=True, help='Path to input JSON file')
parser.add_argument('-o', '--output', type=str, required=True, help='Path to output CSV file')

# 解析命令行参数
args = parser.parse_args()

# 读取JSON文件
with open(args.input, 'r') as f:
    data = json.load(f)

# 将JSON转换为DataFrame对象
df = pd.json_normalize(data, 'logs')

# 将数据保存为CSV文件
df.to_csv(args.output, index=False)

print(f'Successfully converted {args.input} to {args.output}')
