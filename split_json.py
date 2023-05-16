import json
import os
import argparse
from tqdm import tqdm

def split_json(input_file, output_dir, chunk_size):
    # 读取JSON文件
    with open(input_file) as f:
        data = json.load(f)

    # 计算总行数和每个块的大小
    total_rows = len(data)
    rows_per_chunk = min(total_rows, chunk_size)

    # 分割数据并保存为单独的文件
    file_sizes = []
    file_names = []
    for i in tqdm(range(0, total_rows, rows_per_chunk), desc="Splitting"):
        # 确定输出文件路径
        output_path = os.path.join(os.path.expanduser(output_dir), f"output_{i}.json")
        # 将块保存为JSON文件
        with open(output_path, 'w') as f:
            json.dump(data[i:i+rows_per_chunk], f, indent=2)
        # 记录生成文件名和大小
        file_names.append(output_path)
        file_sizes.append(os.path.getsize(output_path))

    print("\nGenerated files:")
    for i, fn in enumerate(file_names):
        size_mb = file_sizes[i] / (1024 * 1024)
        print(f"{fn} ({size_mb:.2f} MB)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split JSON file into smaller chunks')
    parser.add_argument('-i', '--input', type=str, default='~/Desktop/input.json', help='Path to input JSON file (default: ~/Desktop/input.json)')
    parser.add_argument('-o', '--output', type=str, default='~/Desktop/output/', help='Path to output directory (default: ~/Desktop/output/)')
    parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 200000)')

    args = parser.parse_args()

    input_file = os.path.expanduser(args.input)
    output_dir = os.path.expanduser(args.output)
    chunk_size = args.chunk_size

    split_json(input_file, output_dir, chunk_size)
