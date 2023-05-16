# https://github.com/BlueSkyXN/json-to-csv
import os
import argparse
from tqdm import tqdm

def split_text(input_file, output_dir, chunk_size):
    # 打开文本文件并逐行读取
    with open(input_file) as f:
        for i, line in enumerate(tqdm(f, desc="Processing lines")):
            if i % chunk_size == 0:
                # 确定输出文件路径
                output_path = os.path.join(os.path.expanduser(output_dir), f"output_{i//chunk_size}.txt")
                # 如果已经有一个打开的输出文件，关闭它
                if i > 0:
                    f_out.close()
                # 打开新的输出文件
                f_out = open(output_path, 'w')
            # 将行写入输出文件
            f_out.write(line)
        # 关闭最后一个打开的输出文件
        f_out.close()

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
