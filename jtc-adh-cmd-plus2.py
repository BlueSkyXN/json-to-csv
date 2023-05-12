import pandas as pd
import ijson
import os
from tqdm import tqdm
import argparse

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='Convert JSON query log to CSV format')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json") ,required=False, help='Path to input JSON file')

# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv") ,required=False, help='Path to output CSV file')

# 解析命令行参数
args = parser.parse_args()
print(args.input, args.output)

# 使用ijson逐步解析JSON文件并转换为DataFrame
with open(args.input, 'rb') as f:
    # 用列表推导式替换每行末尾的换行符
    objects = [obj.rstrip().replace(b'\n', b',') + b'}' for obj in f if obj.strip() != b'']
    df = pd.read_json(b'[' + b','.join(objects) + b']')

# 在循环中逐行读取数据并添加到DataFrame中
for _, row in tqdm(df.iterrows(), total=len(df), desc="Converting"):
    pass
# 将数据保存为CSV文件
abs_output_path = os.path.abspath(args.output)
df.to_csv(abs_output_path, index=False)

# 打印输出路径
print(f"\n已将JSON数据成功转换并保存到文件：{abs_output_path}")
