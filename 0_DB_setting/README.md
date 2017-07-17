# データベース，テーブルの準備

ここでは，データベースの仕様と作成方法を説明します．

## データベース，テーブルの構造

- 動作に必要なデータベースは次のような構造にしてください．

### 参考・データベースの構造

この作業により作成されるデータベースは、次の通りです。

```
+--------------------+
| Database           |
+--------------------+
| gpsdata            |
+--------------------+

+-----------+----------+------+-----+---------+-------+
| Field     | Type     | Null | Key | Default | Extra |
+-----------+----------+------+-----+---------+-------+
| Date      | datetime | YES  | UNI | NULL    |       |
| Latitude  | double   | YES  |     | NULL    |       |
| Longitude | double   | YES  |     | NULL    |       |
| Altitude  | double   | YES  |     | NULL    |       |
| Speed     | double   | YES  |     | NULL    |       |
| Distance  | double   | YES  |     | NULL    |       |
+-----------+----------+------+-----+---------+-------+
```

- `0_DB_setting/table_settiing.py`には，これを自動的に行うプログラムを用意しています．
  - 事前に，ユーザーとデータベースの作成が必要です．

    1. ユーザー作成例
      ``` sql
      # root ユーザーで
      mysql>CREATE USER
          -> 'USERNAME' identified by 'PASSWORD';
      ```
        - `USERNAME`, `PASSWORD` は適宜決めてください．

    2. データベース作成例
      ``` sql
      # root ユーザーで
      mysql>CREATE DATABASE 'healthchecker' DEFAULT CHARACTER SET utf8;
      mysql>GRANT ALL PRIVILEGES ON 'healthchecker'.* TO 'USERNAME';
      mysql>FLUSH PRIVILEGES;
      mysql>FLUSH PRIVILEGES;
      ```
        - `USERNAME`, `PASSWORD` は上で決めたものを入力してください．

  - 必要に応じて，変更を加えて，利用してください．

## データベース接続情報の保存

設定した情報を`~/.bashrc`などに次のように保存します．
```
export HEALTHCHECKER_HOST='localhost'
export HEALTHCHECKER_DATABASE='healthchecker'
export HEALTHCHECKER_USER='USERNAME'
export HEALTHCHECKER_PASSWD='PASSWORD'
```
- `localhost` は，運用状況に合わせtえ書き換えてください．
- `USERNAME`, `PASSWORD` は上で決めたものを入力してください．

- これら環境変数に保存した接続情報は`db_info.py`から取り出して遣います．
