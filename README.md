# convertert_srt2csv
Convert whisperX's srt file to tsv.

# 実行方法

1. 変換したいデータフォルダを `./data/raw`ディレクトリにいれる。  
この際,必ず下記のようにsrtファイルがrawディレクトリの二つ下にあること。  
例: `./data/raw/508_ジョン・ウィック/508_ジョン・ウィック.srt`

2. 以下の実行コマンドを実行する。  
`python convert_execution.py`

3. `./data/out/`　ディレクトリにcsvに変換されたファイルが出力される。
