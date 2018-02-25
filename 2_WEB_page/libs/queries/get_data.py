# -*- coding: utf-8 -*-
from peewee import *
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.pardir)
from db_schema import *

db = MySQLDatabase(
    host=db_info.HOST,
    database=db_info.NAME,
    user=db_info.USER,
    password=db_info.USER_PASSWORD
)


class MeasuringData:

    # 1時間ごとの合計値を算出
    def hourly_data(self, start_day, goal_day):
        # クエリ作成
        query = (
            Measuring.select(
                fn.HOUR(Measuring.date).alias('oclock'),
                R("SUM(" + Clumn.measuring.distance + ")").alias('distance')
            )
            .where(Measuring.date.between(start_day, goal_day))
            .group_by(fn.HOUR(Measuring.date))
        )
        # データの取得，リストに格納
        return [obj for obj in query]

    # 通過した点を抽出
    def point_data(self, start_day, goal_day):
        # クエリ作成
        query = (
            Measuring.select(
                Measuring.date.alias('date'),
                Measuring.latitude.alias('latitude'),
                Measuring.longitude.alias('longitude')
            )
            .having(
                ((Measuring.date >= start_day) & (Measuring.date <= goal_day))
            )
            .group_by(Measuring.date)
            .order_by(Measuring.date)
        )
        # データの取得，リストに格納
        return [obj for obj in query]


if __name__ == "__main__":

    # デバッグ用
    start = "2016/05/24 00:00"
    goal = "2016/05/24 20:59"

    measuring = MeasuringData()

    measuring_datas = measuring.hourly_data(start_day=start, goal_day=goal)
    for d in measuring_datas:
        print d.date, d.distance
    #
    # measuring_datas = measuring.point_data(start_day,goal_day)
    # for d in measuring_datas:
    #     print d.date, d.latitude, d.longitude
