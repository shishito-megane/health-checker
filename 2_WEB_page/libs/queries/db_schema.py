# -*- coding: utf-8 -*-
import os
from peewee import *
from datetime import date
import sys
sys.path.append(os.pardir)
import db_info

# データベース接続
db = MySQLDatabase(
    host=db_info.HOST,
    database=db_info.NAME,
    user=db_info.USER,
    password=db_info.USER_PASSWORD
)


class Clumn:

    # カラム名との対応を取る
    class measuring:
        date = "Date"
        latitude = "Latitude"
        longitude = "Longitude"
        altitude = "Altitude"
        speed = "Speed"
        distance = "Distance"


class Measuring(Model):

    date = DateTimeField(unique=True,primary_key=True)
    latitude = TextField(db_column= Clumn.measuring.latitude)
    longitude = TextField(db_column= Clumn.measuring.longitude)
    altitude = TextField(db_column= Clumn.measuring.altitude)
    speed = TextField(db_column= Clumn.measuring.speed)
    distance = TextField(db_column= Clumn.measuring.distance)

    class Meta:
        database = db
