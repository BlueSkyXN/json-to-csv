import pandas as pd
import json
import os

# 读取JSON文件并处理
input_path = 'input.json'
with open(input_path, 'r') as f:
    content = f.read().replace('\n', ',')
    json_content = f'[{content[:-1]}]'

data = json.loads(json_content)

# 将JSON转换成DataFrame对象
df = pd.DataFrame(data)

# 将数据保存为CSV文件
output_path = 'output.csv'
abs_output_path = os.path.abspath(output_path)
df.to_csv(abs_output_path, index=False)

# 输出保存路径
print(f'已将JSON数据成功转换并保存到文件：{abs_output_path}')
