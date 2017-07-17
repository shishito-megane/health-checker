# -*- coding:utf-8 -*-
# 距離計算プログラム
from math import sin, cos, acos, radians
earth_rad = 6378.137

def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

def dist_on_sphere(pos0, pos1, radious=earth_rad):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radious

# Osaka = 34.702113, 135.494807
# Tokyo = 35.681541, 139.767103
# London = 51.476853, 0.0
#
# print(dist_on_sphere(Osaka, Tokyo)) # 403.63km
# print(dist_on_sphere(London, Tokyo)) # 9571.22km
