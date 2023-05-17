import vaex
import argparse
import os

parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json"), required=False, help='Path to input JSON file')
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv"), required=False, help='Path to output CSV file')
parser.add_argument('-s', '--chunk_size', type=int, default=10000, required=False, help='Number of lines to process at a time')
args = parser.parse_args()

chunk_size = args.chunk_size
with vaex.open(args.input, convert=True) as df:
    df.export(args.output, progress=True)

abs_output_path = os.path.abspath(args.output)
print(f'Successfully converted {args.input} to {abs_output_path}')
