# -*- coding:utf-8 -*-
# 距離計算プログラム
from math import sin, cos, acos, radians
EARTH_RAD = 6378.137


def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)


def dist_on_sphere(pos0, pos1, radious=EARTH_RAD):
    """
    2地点間の距離を計算します．
    :param pos0: 開始地点の座標(latitude,longtitude)
    :param pos1: 終了地点の座標(latitude,longtitude)
    :param radious: 地球の半径
    """
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radious
