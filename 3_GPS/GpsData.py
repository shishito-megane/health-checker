# -*- coding: utf-8 -*-

import os
from gps import *
from time import *
import time
import threading
import csv

# 参考: https://gist.github.com/wolfg1969/4653340

# 作業ディレクトリの変更
os.chdir("../4_Data")

# ファイルオープン
f = open('data.csv','ab')
csvWriter =csv.writer(f)

# グローバル変数の設定
gpsd = None

# ターミナルのクリア
os.system('clear')

# スレッドの定義
class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True

  def run(self):
    global gpsd,gpstime
    while gpsp.running:
        gpsd.next()                                                             # 初期化
        gpetime = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        gpstime = gpsd.utc[0:4] +'-'+ gpsd.utc[5:7] +'-'+ gpsd.utc[8:10] + ' ' + gpsd.utc[11:19]

if __name__ == '__main__':

    # スレッドの開始
    gpsp = GpsPoller()
    try:
        gpsp.start()
        val=0
        count = 0
        point0 = 0,0
        point1 = 0,0

        # 信号が落ち着くのを待ってから開始
        while (count < 100):
            os.system('clear')

            listData=[]

            csvWriter.writerow(
                [gpstime,gpsd.fix.latitude,gpsd.fix.longitude,gpsd.fix.altitude,gpsd.fix.speed,distance]
            )

            # --- 表形式の結果表示 ---
            #var=1
            #while var==1:
            #print ' GPS reading'
            #print '----------------------------------------'
            #time.sleep(3)
            #print 'latitude ' , gpsd.fix.latitude        #緯度
            #print 'longitude ' , gpsd.fix.longitude      #経度
            #print 'altitude (m)' , gpsd.fix.altitude     #高度
            #print 'eps         ' , gpsd.fix.eps
            #print 'epx         ' , gpsd.fix.epx
            #print 'epv         ' , gpsd.fix.epv
            #print 'ept         ' , gpsd.fix.ept
            #print 'speed (m/s) ' , gpsd.fix.speed        #スピード
            #print 'climb       ' , gpsd.fix.climb
            #print 'track       ' , gpsd.fix.track
            #print 'mode        ' , gpsd.fix.mode
            #print
            #print 'sats        ' , gpsd.satellites

            # --- 一行結果表示 ---
            print  gpstime,gpsd.fix.latitude,gpsd.fix.longitude,gpsd.fix.altitude,gpsd.fix.speed,distance

            # 5秒ごとに観測結果を拾う
            time.sleep(5)
            count += 1


    except (KeyboardInterrupt, SystemExit):
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join()
    print "Done.\nExiting."
