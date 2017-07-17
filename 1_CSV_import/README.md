# データベースへの測定値インポート

このディレクトリのファイルは，`4_Data`にある観測結果をWEBサーバで表示できるようデータベースへ入れます．
インストール先のOSのcron/crontabの機能を使って，`1_CSV_import/data_import.py`を適宜実行するよう設定してください．

設定例:
``` bash
$ crontab -e
```
```  
`*/10 * * * * python /health-checker/1.CSVtoDB-import/data_import.py > /health-checker/log.txt 2>&1`  
```
詳しい設定方法は、その他ドキュメントを参考にしてください。
