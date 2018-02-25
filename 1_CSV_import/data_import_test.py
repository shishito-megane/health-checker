# -*- coding: utf-8 -*-
# テスト用のCSVサンプルデータをDBへインポートするプログラム
import csv
import sys
import os
sys.path.append(os.pardir)
import db_info
import MySQLdb

# 計測したGPSデータが入っているディレクトリへ
os.chdir("../4_Data")

connection = MySQLdb.connect(
    host=db_info.HOST,
    database=db_info.NAME,
    user=db_info.USER,
    password=db_info.USER_PASSWORD
)

cursor = connection.cursor()

# データファイル読み込み
with open("test_data.csv", "r") as input_file:

    reader = csv.reader(input_file)
    # # ヘッダーは飛ばす
    # header = next(reader)
    # csvファイルを1行ずつ読み込んでデータベースに入れる。
    for row in reader:
        sql = "INSERT IGNORE INTO  measuring values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (row[0], row[1], row[2], row[3], row[4], row[5]))

connection.commit()

cursor.close()
connection.close()
