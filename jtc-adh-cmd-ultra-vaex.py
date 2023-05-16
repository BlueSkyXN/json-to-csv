import vaex
import argparse
import os

parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input JSON file')
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv"), required=False, help='Path to output CSV file')
parser.add_argument('-s', '--chunksize', type=int, default=10000, required=False, help='Number of lines to process at a time')
args = parser.parse_args()

chunksize = args.chunksize
df = vaex.from_json(args.input, chunk_size=chunksize)

abs_output_path = os.path.abspath(args.output)
if os.path.isfile(abs_output_path):
    df.export(abs_output_path, mode='a', header=False)
else:
    df.export(abs_output_path)

print(f'Successfully converted {args.input} to {abs_output_path}')
