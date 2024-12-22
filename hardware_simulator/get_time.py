import os
import pandas as pd

# 设置根目录路径
root_dir = '/opt/data/private/Lightening-Transformer-AE/hardware_simulator/results/energy_latency_all'
output_file = './output_energy_latency.csv'  # 结果输出文件路径

# 初始化结果列表
results = []

# 遍历所有子目录及文件
for model_dir in os.listdir(root_dir):
    model_path = os.path.join(root_dir, model_dir)
    if os.path.isdir(model_path):  # 确保是目录
        for config_dir in os.listdir(model_path):
            config_path = os.path.join(model_path, config_dir)
            if os.path.isdir(config_path):
                total_csv_path = os.path.join(config_path, 'total.csv')
                if os.path.exists(total_csv_path):
                    # 读取 total.csv 文件中的数据
                    df = pd.read_csv(total_csv_path)
                    # 提取 total energy 和 total latency 行的值
                    total_energy = df[df.iloc[:, 0] == 'total'].iloc[0, 1]  # 第一列对应 energy
                    total_latency = df[df.iloc[:, 0] == 'total'].iloc[0, 2]  # 第二列对应 latency
                    
                    # 将结果存储到列表中
                    results.append({
                        'model': model_dir,
                        'config': config_dir,
                        'total_energy (mJ)': total_energy,
                        'total_latency (ms)': total_latency
                    })

# 将结果写入指定的 CSV 文件
output_df = pd.DataFrame(results)
output_df.to_csv(output_file, index=False)

print(f"Results have been saved to {output_file}")
