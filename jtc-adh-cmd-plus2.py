import ijson
import json
import pandas as pd
import argparse
import os

# 创建参数解析器
parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json") ,required=False, help='Path to input JSON file')
# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv") ,required=False, help='Path to output CSV file')

args = parser.parse_args()

data = []
with open(args.input, 'r') as f:
    for line in f:
        try:
            obj = json.loads(line.strip())
            data.append(obj)
        except Exception as e:
            print(f'Error occurred: {e}')

df = pd.DataFrame(data)

# 将DataFrame写入CSV文件
abs_output_path = os.path.abspath(args.output)
df.to_csv(abs_output_path, index=False)
print(f'Successfully converted {args.input} to {abs_output_path}')