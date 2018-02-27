# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
# ライブラリパスの登録
import sys, os, os.path
APP_PATH = os.path.dirname(__file__)
LIBS_PATH = os.path.join(APP_PATH, 'libs')
if LIBS_PATH not in sys.path:
    sys.path.append(LIBS_PATH)
from libs.bottle import *
from libs.parameters.term import Parameter
from libs.queries.get_data import MeasuringData
from libs.entities.molding import *
from libs.evaluation import judge
# import libs.db_info as db_info
# import json
# from datetime import *


# === bootstrapなどの共通ファイルを読み込む ===
@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')


@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')


@route('/fonts/<filename>')
def fonts_static(filename):
    return static_file(filename, root='./fonts')


@route('/css/<filename>')
def css_static(filename):
    return static_file(filename, root='./css')


# === トップ・ログインページ ===
@route('/health/top')
@view("top.tpl")
def database():

    # ヘッター，フッター，メニューバーあたりの設定
    title = "ヘルス☆チェッカー | ログイン"
    link = "/helath/today"
    footer = "© 2017 Shishito Megane. All rights reserved."

    return dict(
        title=title, link=link, footer=footer
    )


# === 今日の活動ページ ===
@route('/health/today')
@view("today.tpl")
def database():

    # ヘッター，フッター，メニューバーあたりの設定
    title = "ヘルス☆チェッカー | 今日のあなた"
    footer = "© 2017 Shishito Megane. All rights reserved."

    # GETパラメータの取得
    name = request.query.name
    sex = request.query.sex
    height = request.query.height

    if name == "":
        name = "ゲスト"
    if sex == "":
        sex = "man"
    if height == "":
        height = "165"
    height = float(height)
    param = Parameter(
        start_str='2016/04/22', goal_str='2016/06/24'
    )

    # データの取得
    hourly_data = MeasuringData().hourly_data(
        param.start_day, param.goal_day
    )
    point_data = MeasuringData().point_data(
        param.start_day, param.goal_day
    )

    # データの成形
    span = get_daily_span(hourly_data)
    graph_dataset, table_dataset, m = format_datas(
        hourly_data, point_data, height
    )

    # 判定
    lev, lev_img, lev_msg = judge(
        sex, table_dataset["sum_hosu"]
    )

    return dict(
        title=title, footer=footer,
        name=name, sex=sex, height=height,
        span=span,
        graph_dataset=graph_dataset, table_dataset=table_dataset,
        lev_img=lev_img, lev_msg=lev_msg
    )


# === 今日の移動地図===
@route('/health/detail')
@view("detail.tpl")
def database():

    # ヘッター，フッター，メニューバーあたりの設定
    title = "ヘルス☆チェッカー | 移動履歴"
    footer = "© 2017 Shishito Megane. All rights reserved."

    # GETパラメータの取得
    name = request.query.name
    sex = request.query.sex
    height = request.query.height
    if name == "":
        name = "ゲスト"
    if sex == "":
        sex = "man"
    if height == "":
        height = "165"
    height = float(height)
    param = Parameter(
        start_str='2016/04/22', goal_str='2016/06/24'
    )

    # データの取得
    hourly_data = MeasuringData().hourly_data(
        param.start_day, param.goal_day
    )
    point_data = MeasuringData().point_data(
        param.start_day, param.goal_day
    )
    # データの成形
    graph_dataset, t, map_dataset = format_datas(
        hourly_data, point_data, height
    )

    return dict(
        title=title, footer=footer,
        name=name, sex=sex, height=height,
        map_dataset=map_dataset
    )


# === エラーページの対応 ===
# Internal Server Errorの場合
@error(500)
def error_500(error):

    return """
    データ表示期間内に、サーバに問題があったか、データ表示期間に間違いがある可能性があります。
    ブラウザの戻るボタンから、前のページに戻ってください。
    それでもこのメッセージが表示される場合は、管理者にお問い合わせください。
    """


if __name__ == "__main__":
    # コマンドラインから起動した場合
    run(host='0.0.0.0', port=8080, debug=True)

else:
    # WEBサーバーアプリケーションから起動した場合
    application = default_app()
