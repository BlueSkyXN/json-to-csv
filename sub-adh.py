# https://github.com/BlueSkyXN/json-to-csv
import argparse
import pandas as pd
import os
from tqdm import tqdm

# 创建一个ArgumentParser对象
parser = argparse.ArgumentParser(description='Split text file into smaller chunks and convert to CSV format')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input file')

# 添加输出目录路径参数
parser.add_argument('-o', '--output_dir', type=str, default=os.path.expanduser("~/Desktop/output/"), required=False, help='Path to output directory')

# 添加切割参数
parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 200000)')

# 解析命令行参数
args = parser.parse_args()
print(args.input, args.output_dir)

# 每个小文件的大小（以行数为单位）
chunk_size = args.chunk_size

# 获取输入文件大小
input_file_size = os.path.getsize(args.input)

# 创建输出目录，如果目录不存在
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

# 切割大文件
with open(args.input) as f:
    i = 0
    while True:
        # 确定输出文件路径
        output_path = os.path.join(args.output_dir, f"output_{i}.txt")

        with open(output_path, 'w') as f_out:
            data = []
            for j, line in tqdm(enumerate(f), total=chunk_size, desc=f"Converting chunk {i+1}"):
                if j >= chunk_size:
                    break
                data.append(line.strip())

            # 如果当前块不为空，则保存文本文件并转换为CSV格式
            if len(data) > 0:
                f_out.write('\n'.join(data))

                # 转换为CSV格式并将结果保存到输出目录
                with open(output_path) as f_in:
                    df = pd.read_json(f_in, lines=True)

                # 如果当前文件中包含有效数据，则保存为CSV文件
                if len(df) > 0:
                    abs_output_path = os.path.abspath(os.path.join(args.output_dir, f"output_{i}.csv"))
                    with open(abs_output_path, 'w') as f_out_csv:
                        df.to_csv(f_out_csv, index=False)

                    print(f"{abs_output_path} ({os.path.getsize(abs_output_path) / (1024 * 1024):.2f} MB)")

                else:
                    print(f"{output_path} is empty, removing file")
                    os.remove(output_path)

            # 如果当前块为空，则删除该文件
            else:
                print(f"{output_path} is empty, removing file")
                os.remove(output_path)

        i += 1

        # 如果已经读到了文件的末尾，则退出循环
        if not line:
            break

# 打印输出目录路径
print(f"\n已将输入文件成功转换并保存到目录：{args.output_dir}")
