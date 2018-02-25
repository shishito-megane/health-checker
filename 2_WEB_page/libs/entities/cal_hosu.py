# -*- coding:utf-8 -*-
# 歩数計算サンプルプログラム


def convert(distance, height):
    """
    歩数を計算します．
    :param distance: 移動距離[m]
    :param height: 身長[cm]
    """
    # 速度係数 普通歩き: 0.45
    speed_factor = 0.45
    result = distance * 1000 / (height * 0.01 * speed_factor)
    return result
