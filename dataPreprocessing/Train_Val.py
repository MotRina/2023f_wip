import os
import shutil
import random

# パス設定
data_dir = "/Users/rinamotoyama/Downloads/github/2023f_wip/learning/data"
train_dir = "/Users/rinamotoyama/Downloads/github/2023f_wip/learning/train"
test_dir = "/Users/rinamotoyama/Downloads/github/2023f_wip/learning/val"

# ディレクトリ作成
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for gender in ["female", "male"]:
    gender_dir = os.path.join(data_dir, gender)
    folders = [d for d in os.listdir(gender_dir) if os.path.isdir(os.path.join(gender_dir, d))]

    # ランダムに分割
    random.shuffle(folders)
    split_point = int(len(folders) * 0.75)  # 75%を学習データに
    train_folders = folders[:split_point]
    test_folders = folders[split_point:]

    # 学習データの処理
    train_gender_dir = os.path.join(train_dir, gender)
    os.makedirs(train_gender_dir, exist_ok=True)
    for folder in train_folders:
        folder_path = os.path.join(gender_dir, folder)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, train_gender_dir)

    # 検証データの処理
    test_gender_dir = os.path.join(test_dir, gender)
    os.makedirs(test_gender_dir, exist_ok=True)
    for folder in test_folders:
        folder_path = os.path.join(gender_dir, folder)
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, test_gender_dir)
