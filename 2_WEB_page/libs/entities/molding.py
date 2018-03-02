# -*- coding:utf-8 -*-
# グラフと表のデータを成形するモジュール
from cal_hosu import convert


# 日付リストの成形
def get_daily_span(hourly_data):
    """
    グラフ表示用に日付の文字列リストの作成をします．
    """

    date_list = {
        "date": [str(d.oclock) for d in hourly_data]
    }
    return date_list


# 計測データリストの成形
def format_datas(hourly_data, point_data, height):
    """
    グラフ表示用に計測データのリストを作成します．
    """

    distance = [d.distance for d in hourly_data]
    hosu = [convert(d, height) for d in distance]

    graph_dataset = {
        "distance": distance,
        "hosu":     hosu
    }
    table_dataset = {
        "sum_distance": sum(distance),
        "sum_hosu":     sum(hosu)
    }
    map_dataset = {
        "latitude":    [d.latitude for d in point_data],
        "longitude":   [d.longitude for d in point_data]
    }

    return graph_dataset, table_dataset, map_dataset
