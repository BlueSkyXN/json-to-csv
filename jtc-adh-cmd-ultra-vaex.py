import vaex
import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input JSON file')
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv"), required=False, help='Path to output CSV file')
parser.add_argument('-s', '--chunk_size', type=int, default=10000, required=False, help='Number of lines to process at a time')
args = parser.parse_args()

chunk_size = args.chunk_size

# Create an empty Vaex DataFrame
df_vaex = None

# Read the input file in chunks using pandas, then convert each chunk to a Vaex DataFrame
for chunk in pd.read_json(args.input, lines=True, chunksize=chunk_size):
    chunk_vaex = vaex.from_pandas(chunk, copy_index=False)
    if df_vaex is None:
        df_vaex = chunk_vaex
    else:
        df_vaex = df_vaex.concat(chunk_vaex)

abs_output_path = os.path.abspath(args.output)
if os.path.isfile(abs_output_path):
    df_vaex.export(abs_output_path, mode='a', header=False)
else:
    df_vaex.export(abs_output_path)

print(f'Successfully converted {args.input} to {abs_output_path}')
