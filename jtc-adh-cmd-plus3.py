import ijson
import pandas as pd
import os
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='Convert large JSON file to CSV format')

# 添加输入文件路径参数
parser.add_argument('-i', '--input', type=str, default='querylog.json', required=False,
                    help='Path to input JSON file')

# 添加输出文件路径参数
parser.add_argument('-o', '--output', type=str, default='large_data.csv', required=False,
                    help='Path to output CSV file')

# 解析命令行参数
args = parser.parse_args()

def parse_json(input_path, output_path):
    # 打开输入文件和输出文件
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        # 逐行读取JSON数据
        for line in input_file:
            # 将每行数据转换为json对象
            obj = json.loads(line.strip())
            # 将json对象以标准格式写回输出文件，并添加换行符
            output_file.write(json.dumps(obj) + '\n')

    # 使用ijson解析JSON文件并转换为DataFrame对象
    with open(output_path, 'r') as input_file:
        # 逐行读取JSON数据
        objects = ijson.items(input_file, 'item')
        # 将JSON数据转换为DataFrame对象
        df = pd.DataFrame(objects)

    # 将数据保存为CSV文件
    abs_output_path = os.path.abspath(output_path)
    csv_path = os.path.splitext(abs_output_path)[0] + '.csv'
    df.to_csv(csv_path, index=False)

    print(f'已将JSON数据成功转换并保存到文件：{csv_path}')
