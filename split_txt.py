# https://github.com/BlueSkyXN/json-to-csv
import os
import argparse
from tqdm import tqdm

def split_text(input_file, output_dir, chunk_size):
    # 打开文本文件并逐行读取
    with open(input_file) as f:
        for i, line in enumerate(f):
            if i % chunk_size == 0:
                # 确定输出文件路径
                output_path = os.path.join(os.path.expanduser(output_dir), f"output_{i}.txt")
                # 将块保存为文本文件
                with open(output_path, 'w') as f_out:
                    data = []
                    for j, line in enumerate(f):
                        if j >= chunk_size:
                            break
                        data.append(line.strip())
                    for item in data:
                        f_out.write(item + '\n')
                
                print(f"{output_path} ({os.path.getsize(output_path) / (1024 * 1024):.2f} MB)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split text file into smaller chunks')
    parser.add_argument('-i', '--input', type=str, default='~/Desktop/input.txt', help='Path to input text file (default: ~/Desktop/input.txt)')
    parser.add_argument('-o', '--output', type=str, default='~/Desktop/output/', help='Path to output directory (default: ~/Desktop/output/)')
    parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 200000)')

    args = parser.parse_args()

    input_file = os.path.expanduser(args.input)
    output_dir = os.path.expanduser(args.output)
    chunk_size = args.chunk_size

    split_text(input_file, output_dir, chunk_size)
