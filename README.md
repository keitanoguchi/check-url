### Usage

python ファイルを実行
```sh
$ python main.py
```

出力例
```
---------- Google ----------
[OK] https://www.google.com/
  code: 200

---------- Yahoo ----------
[OK] https://www.yahoo.co.jp/hoge
  code: 404
  reason: Not Found

[Alert] https://news.yahou.co.jp/
  code: N/A
  reason: [Errno 8] nodename nor servname provided, or not known

---------- tenki.jp ----------
[OK] https://tenki.jp/
  code: 200
```
