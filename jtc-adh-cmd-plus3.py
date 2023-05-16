import ijson
import json
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
    with open(input_path, 'r') as input_file:
        # 读取所有行并组成一个列表
        lines = input_file.readlines()

        # 将列表中的所有行连接成一个字符串（去掉回车符）
        data_str = ''.join(lines).replace('\n', '')

        # 解析JSON数组
        objects = json.loads('[' + data_str + ']')

    # 将JSON数据转换为DataFrame对象
    df = pd.DataFrame(objects)

    # 将数据保存为CSV文件
    abs_output_path = os.path.abspath(output_path)
    csv_path = os.path.splitext(abs_output_path)[0] + '.csv'
    df.to_csv(csv_path, index=False)

    print(f'已将JSON数据成功转换并保存到文件：{csv_path}')

if __name__ == '__main__':
    # 解析命令行参数
    args = parser.parse_args()

    # 调用 parse_json 函数并传递输入文件路径和输出文件路径
    parse_json(args.input, args.output)
