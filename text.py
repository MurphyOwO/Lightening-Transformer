import os

# 指定路径
base_path = "/opt/data/private/Lightening-Transformer-AE/software_model/data/train"

# 获取所有以 "class" 开头的文件夹名称，并按数字部分降序排序
folders = sorted(
    [folder for folder in os.listdir(base_path) if folder.startswith("class")],
    key=lambda x: int(x[5:]),
    reverse=True
)

# 从后往前遍历并重命名
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    # 检查是否是文件夹
    if os.path.isdir(folder_path):
        try:
            # 提取数字部分并加 1
            current_number = int(folder[5:])  # 提取 class 后面的数字
            new_number = current_number + 1
            new_folder_name = f"class{new_number}"
            
            # 构造新文件夹路径
            new_folder_path = os.path.join(base_path, new_folder_name)
            
            # 重命名文件夹
            os.rename(folder_path, new_folder_path)
            print(f"Renamed {folder} -> {new_folder_name}")
        except ValueError:
            print(f"Skipping {folder}: not a valid class folder.")
