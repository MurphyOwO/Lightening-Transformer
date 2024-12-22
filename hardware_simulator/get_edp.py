import pandas as pd
# 读取现有的CSV文件
file_path = '/opt/data/private/Lightening-Transformer-AE/hardware_simulator/output_energy_latency.csv'
df = pd.read_csv(file_path)

# 计算 EDP = Energy * Latency
df['edp (mJ*ms)'] = df['total_energy (mJ)'] * df['total_latency (ms)']

# 保存新的CSV文件，包含计算后的 EDP 列
output_file_with_edp = './output_energy_latency_with_edp.csv'
df.to_csv(output_file_with_edp, index=False)

# 显示更新后的DataFrame
df.head()
