import ijson
import json
import pandas as pd
import argparse
import os
from itertools import islice

def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield list(islice(iterator, size))

parser = argparse.ArgumentParser(description='Convert JSON file to CSV file')
parser.add_argument('-i', '--input', type=str, default=os.path.expanduser("~/Desktop/input.json") ,required=False, help='Path to input JSON file')
parser.add_argument('-o', '--output', type=str, default=os.path.expanduser("~/Desktop/output.csv") ,required=False, help='Path to output CSV file')
parser.add_argument('-s', '--chunksize', type=int, default=10000, required=False, help='Number of lines to process at a time')
args = parser.parse_args()

data = []
with open(args.input, 'r') as f:
    for chunk in chunks(f, args.chunksize):
        for line in chunk:
            try:
                obj = json.loads(line.strip())
                data.append(obj)
            except Exception as e:
                print(f'Error occurred: {e}')

        df = pd.DataFrame(data)
        abs_output_path = os.path.abspath(args.output)
        if os.path.isfile(abs_output_path):
            df.to_csv(abs_output_path, mode='a', header=False, index=False)
        else:
            df.to_csv(abs_output_path, index=False)

        data = []

print(f'Successfully converted {args.input} to {abs_output_path}')
