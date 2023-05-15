import argparse
import pandas as pd
import os
from tqdm import tqdm
import json

parser = argparse.ArgumentParser(description='Split text file into smaller chunks and convert to CSV format')
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input file')
parser.add_argument('-o', '--output_dir', type=str, default=os.path.expanduser("~/Desktop/output/"), required=False, help='Path to output directory')
parser.add_argument('-s', '--chunk_size', type=int, default=200000, help='Chunk size (default: 200000)')

args = parser.parse_args()

chunk_size = args.chunk_size

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

with open(args.input) as f:
    i = 0
    while True:
        output_path = os.path.join(args.output_dir, f"output_{i}.csv")
        data = []

        for j, line in tqdm(enumerate(f), total=chunk_size, desc=f"Converting chunk {i+1}"):
            if j >= chunk_size:
                break
            data.append(json.loads(line.strip()))

        if data:
            df = pd.DataFrame(data)

            if len(df) > 0:
                df.to_csv(output_path, index=False)
                print(f"{output_path} ({os.path.getsize(output_path) / (1024 * 1024):.2f} MB)")

        if j < chunk_size-1:
            break

        i += 1
