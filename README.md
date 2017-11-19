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
  DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS"
  ```

- Python, Pythonライブラリ
  - anaconda を使用して，環境を構築します．
  - 環境構築の設定ファイルは，environment.yml を使用してください．
  - conda自体の設定は，その他のドキュメントを参考にしてください．必要なモジュールは次のとおりです．

    ``` bash
    $ conda list
    alabaster                 0.7.10                   py27_0  
    babel                     2.4.0                    py27_0  
    docutils                  0.13.1                   py27_0  
    gps3                      0.33.3                    <pip>
    imagesize                 0.7.1                    py27_0  
    jinja2                    2.9.6                    py27_0  
    markupsafe                0.23                     py27_2  
    mysql-python              1.2.5                    py27_0  
    openssl                   1.0.2l                        0  
    peewee                    2.10.1                   py27_0    conda-forge
    pip                       9.0.1                    py27_1  
    pygments                  2.2.0                    py27_0  
    python                    2.7.13                        0  
    pytz                      2017.2                   py27_0  
    readline                  6.2                           2  
    requests                  2.14.2                   py27_0  
    setuptools                27.2.0                   py27_0  
    six                       1.10.0                   py27_0  
    snowballstemmer           1.2.1                    py27_0  
    sphinx                    1.6.2                    py27_0  
    sphinxcontrib             1.0                      py27_0  
    sphinxcontrib-websupport  1.0.1                    py27_0  
    sqlite                    3.13.0                        0  
    tk                        8.5.18                        0  
    typing                    3.6.1                    py27_0  
    wheel                     0.29.0                   py27_0  
    zlib                      1.2.8                         3   
    ```
  - python3.xでは使用しているライブラリの都合で動かないようです．

- Mysql (MariaDB)

  ``` bash
  $ mysql --version
  mysql  Ver 15.1 Distrib 10.0.31-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2
  ```

  ```
  Server version: 10.0.31-MariaDB-0ubuntu0.16.04.2 Ubuntu 16.04
  ```
- GPSモジュール

  - [ＧＰＳモジュール ＧＭＳ６－ＣＲ６ （９６００ｂｐｓ）(秋月電子)](http://akizukidenshi.com/catalog/g/gM-09252/)


# 利用・配布

自由です．利用により問題が生じても作者は責任を負いません．


