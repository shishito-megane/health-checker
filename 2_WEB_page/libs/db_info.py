"""
データベース接続情報．環境変数から取得します．
"""
# -*- coding:utf-8 -*-
# データベース接続情報
import os

HOST            = os.environ.get("HEALTHCHECKER_HOST")
NAME            = os.environ.get("HEALTHCHECKER_DATABASE")
USER            = os.environ.get("HEALTHCHECKER_USER")
USER_PASSWORD   = os.environ.get("HEALTHCHECKER_PASSWD")
