# -*- coding:utf-8 -*-
# 歩数計算サンプルプログラム
def convert(distance,height):
    result = distance * 1000 / ( height * 0.01 * 0.45 )
    return result
