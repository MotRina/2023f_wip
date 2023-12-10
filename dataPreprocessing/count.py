# female、maleのフォルダ内の画像をカウント

import os
import glob

def count_images(directory):
    # サポートされる画像ファイルの拡張子
    extensions = ['*.jpg', '*.jpeg', '*.png']
    
    total_images = 0

    # 指定されたディレクトリのサブディレクトリを反復処理する
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)

        # サブディレクトリかどうか確認
        if os.path.isdir(subdir_path):
            # サブディレクトリ内の画像ファイルをカウント
            images_count = sum([len(glob.glob(os.path.join(subdir_path, ext))) for ext in extensions])
            total_images += images_count

    return total_images

directory_path = '/Users/rinamotoyama/Downloads/github/2023f_wip/元データ/female'
print(f"Total images: {count_images(directory_path)}")
