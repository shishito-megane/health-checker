# -*- coding: utf-8 -*-
# テスト用のCSVサンプルデータをDBへインポートするプログラム
import csv
import sys
import os
sys.path.append(os.pardir)
import db_info
import MySQLdb

# 作業ディレクトリの変更
os.chdir("../4_Data")

# データベース接続
connection = MySQLdb.connect(
    host    = db_info.HOST,
    user    = db_info.USER,
    passwd  = db_info.USER_PASSWORD,
    db      = db_info.NAME,
)
# カーソル取得
cursor = connection.cursor()

# データファイル読み込み
with open("test_data.csv", "r") as input_file:

	reader = csv.reader(input_file)
	# # ヘッダーは飛ばす
	# header = next(reader)
	# csvファイルを1行ずつ読み込んでデータベースに入れる。
	for row in reader:
		sql = "INSERT IGNORE INTO  measuring values(%s,%s,%s,%s,%s,%s)"
		cursor.execute(sql, (row[0],row[1],row[2],row[3],row[4],row[5]))

# DBへコミット
connection.commit()
# 接続終了
cursor.close()
connection.close()
