"""
日付に関するパラメータの設定を行います．
"""
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class Parameter:

    def __init__(self, start_str, goal_str):
        self.today      = datetime.today()
        # グラフ用に文字型も定義
        self.today_str  = self.today.strftime("%Y年%m月%d日 %H時%M分")
        # データを取得する最初の日
        self.start_day  = self.today-timedelta(days=1)
        # データを取得する最後の日
        self.goal_day   = self.today-timedelta(days=0)

        # 適切なフォーマットに変換
        if (start_str):
            # 日付時刻型のフォーマット
            self.start_day  = datetime.strptime(start_str+" 00:00","%Y/%m/%d %H:%M")
        # 文字型のフォーマット
        self.start_str  = self.start_day.strftime("%Y年%m月%d日 %H時%M分")

        if (goal_str):
            # 日付時刻型のフォーマット
            self.goal_day   = datetime.strptime(goal_str+" 23:59","%Y/%m/%d %H:%M")
        # 文字型のフォーマット
        self.goal_str  = self.goal_day.strftime("%Y年%m月%d日 %H時%M分")
