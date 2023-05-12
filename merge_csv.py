import pandas as pd
import os

# 设置文件夹路径和输出文件名
folder_path = r"C:\Users\xienan\Downloads\Test"
output_file = r"C:\Users\xienan\Downloads\merged_output.csv"

# 列出所有以"output_"开头的csv文件
files = [f for f in os.listdir(folder_path) if f.startswith("output_") and f.endswith(".csv")]

# 读取所有csv文件并将它们合并到一个数据框中
dfs = []
for file in files:
    path = os.path.join(folder_path, file)
    df = pd.read_csv(path)
    dfs.append(df)
merged_df = pd.concat(dfs, ignore_index=True)

# 将合并后的数据保存到输出文件中
merged_df.to_csv(output_file, index=False)
print(f"Merged {len(dfs)} CSV files into {output_file}.")
