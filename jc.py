import pandas as pd
import json

# 读取JSON文件并处理
with open('querylog.json', 'r') as f:
    content = f.read().replace('\n', ',')
    json_content = f'[{content[:-1]}]'

data = json.loads(json_content)

# 将JSON转换成DataFrame对象
df = pd.DataFrame(data)

# 将数据保存为CSV文件
df.to_csv('large_data.csv', index=False)
