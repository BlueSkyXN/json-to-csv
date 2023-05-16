import argparse
import pandas as pd
import json
import os

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='Convert JSON query log to CSV format')
#print(f'debug0')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json") ,required=False, help='Path to input JSON file')
#print(f'debug1')

# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv") ,required=False, help='Path to output CSV file')
#print(f'debug2')

# 解析命令行参数
args = parser.parse_args()
#print(f'debug3')
print(args.input, args.output)


# 读取JSON文件并处理
with open(args.input, 'r') as f:
    content = f.read().replace('\n', ',')
    json_content = f'[{content[:-1]}]'

data = json.loads(json_content)

# 将JSON转换成DataFrame对象
df = pd.DataFrame(data)

# 将数据保存为CSV文件
abs_output_path = os.path.abspath(args.output)
df.to_csv(abs_output_path, index=False)

# 输出保存路径
print(f'已将JSON数据成功转换并保存到文件：{abs_output_path}')
