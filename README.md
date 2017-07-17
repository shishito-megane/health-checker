# Name
health-checker

# Overview
GPS信号を用いた健康診断アプリケーション

# Description
このプログラムは，GPS信号により現在位置を取得し，移動した距離を歩数換算し，健康かどうか診断するアプリケーションです．

# Demo
[結果をブラウザ画面で確認している様子(youtube)](https://www.youtube.com/watch?v=PTSh53S1VRQ)

# Requirements

- OS
  OSは，ubuntu, raspbian での動作を確認しています．その他のLinuxでも僅かな修正で動くと思います．
  ``` bash
  $ cat /etc/lsb-release
  DISTRIB_ID=Ubuntu
  DISTRIB_RELEASE=16.04
  DISTRIB_CODENAME=xenial
  DISTRIB_DESCRIPTION="Ubuntu 16.04.2 LTS"
  ```

- Python, Pythonライブラリ
  - anaconda を使用して，環境を構築します．conda自体の設定は，その他のドキュメントを参考にしてください．必要なモジュールは次のとおりです．

    ``` bash
    $ conda list
    # packages in environment at /anaconda3/envs/healthchecker:
    #
    mysql-python              1.2.5                    py27_0  
    openssl                   1.0.2l                        0  
    peewee                    2.10.1                   py27_0    conda-forge
    pip                       9.0.1                    py27_1  
    python                    2.7.13                        0  
    readline                  6.2                           2  
    setuptools                27.2.0                   py27_0  
    sqlite                    3.13.0                        0  
    tk                        8.5.18                        0  
    wheel                     0.29.0                   py27_0  
    zlib                      1.2.8                         3  
    ```
  - python3.xでは使用しているライブラリの都合で動かないようです．

- Mysql (MariaDB)

  ```
  Your MariaDB connection id is 121
  Server version: 10.0.29-MariaDB-0ubuntu0.16.04.1 Ubuntu 16.04
  ```
- GPSモジュール

  - [ＧＰＳモジュール ＧＭＳ６－ＣＲ６ （９６００ｂｐｓ）(秋月電子)](http://akizukidenshi.com/catalog/g/gM-09252/)


# LICENCE

  © 2017 Shishito Megane. All rights reserved.
