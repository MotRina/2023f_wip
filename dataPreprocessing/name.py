# ファイル名の整理
import os
directory_path = "./data/"

for root, dirs, files in os.walk(directory_path):
   for n, file in enumerate(sorted(files), start=1):
       new_name = os.path.join(root, f"{os.path.basename(root)}_{n}.jpg")
       os.rename(os.path.join(root, file), new_name)
