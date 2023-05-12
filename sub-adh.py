import argparse
import pandas as pd
import os
from tqdm import tqdm

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='Split text file into smaller chunks and convert to CSV format')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input file')

# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv"), required=False, help='Path to output CSV file')

# 添加切割参数
parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 200000)')

# 解析命令行参数
args = parser.parse_args()
print(args.input, args.output)

# 输出目录路径和文件名分开处理，并扩展波浪线
output_dir = os.path.expanduser(args.output)
output_file_name = "output.csv"

# 每个小文件的大小（以行数为单位）
chunk_size = args.chunk_size

# 获取输入文件大小
input_file_size = os.path.getsize(args.input)

# 创建输出目录，如果目录不存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 切割大文件
with open(args.input) as f:
    i = 0
    while True:
        # 确定输出文件路径
        output_path = os.path.join(output_dir, f"output_{i}.txt")
        # 将块保存为文本文件
        with open(output_path, 'w') as f_out:
            data = []
            for j, line in tqdm(enumerate(f), total=chunk_size, desc=f"Converting chunk {i+1}"):
                if j >= chunk_size:
                    break
                data.append(line.strip())
            f_out.write('\n'.join(data))
        
        print(f"{output_path} ({os.path.getsize(output_path) / (1024 * 1024):.2f} MB)")
        i += 1

        # 如果已经读到了文件的末尾，则退出循环
        if not line:
            break

# 对每个小文件进行转换为CSV格式的操作
for j in range(0, i):
    # 拼接当前小文件的名称
    input_file_path = os.path.join(output_dir, f"output_{j}.txt")
    output_file_path = os.path.join(output_dir, output_file_name)

    # 读取txt文件并转换成DataFrame对象
    df = pd.read_csv(input_file_path, sep=" ")

    # 在循环中逐行读取数据并添加到DataFrame中
    for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Converting file {j+1}/{i}"):
        pass

    # 将数据保存为CSV文件
    abs_output_path = os.path.abspath(output_file_path)
    df.to_csv(abs_output_path, index=False)

# 打印输出路径
print(f"\n已将输入文件成功转换并保存到文件：{output_file_path}")
