# -*- coding: utf-8 -*-
# データベースのテーブルを作るプログラム．READMEを参考にしてください．
import sys
import os
sys.path.append(os.pardir)
import db_info
import MySQLdb

connection = MySQLdb.connect(
    host=db_info.HOST,
    database=db_info.NAME,
    user=db_info.USER,
    password=db_info.USER_PASSWORD
)

cursor = connection.cursor()

sql = "CREATE TABLE measuring (Date datetime unique, Latitude double, Longitude double, Altitude double, Speed double, Distance double);"
cursor.execute(sql)

# # 結果表示 for debug
# sql = "show columns from measuring"
# cursor.execute(sql)

cursor.close()
connection.close()
