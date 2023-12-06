# データの前処理
# 動画からフレーム抽出をする

import cv2
import os
import glob

# 動画が保存されているディレクトリ
directory = './data_boar/'

# ディレクトリ内の全てのmp4ファイルを取得
movies = glob.glob(directory + '/*.mp4')

for movie in movies:
    # ファイル名（拡張子なし）を取得
    movie_name = os.path.basename(movie).split('.')[0]
    movie_path = os.path.join(directory, movie_name)

    # 対応するフォルダがなければ作成
    if not os.path.exists(movie_path):
        os.mkdir(movie_path)

    count = 0
    frame_interval = 3  # 3フレームごとに1枚の画像を保存
    cap = cv2.VideoCapture(movie)
    
    while True:
        ret, frame = cap.read()
        if ret:
            # 3フレームごとに画像を保存
            if count % frame_interval == 0:
                img_name = f'{movie_name}_{count:05d}.jpg'
                cv2.imwrite(os.path.join(movie_path, img_name), frame)
            count += 1
        else:
            break

    cap.release()
