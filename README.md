# DJglass  
  
注いだ飲み物にあわせてイケてるミュージックを流すイケイケなグラス

## INSTALL
```
pip install -r requirements.txt
```
please use python3


## HOW TO USE
please use python3.5 or later
```
python dj_glass.py --dummycamera --debug 
```
* --debug : デバッグモード
* --dummycamera : picameraなしで実行代わりにサンプル画像をよみこむ

PCだとpicameraモジュールがインストールできないので`--dummycamera`オプションで実行してください｡
picameraモジュールのインポートを飛ばすのでエラーが出ないはずです｡

ドリンクの認識機能､音楽の再生機能は未実装
ドリンクの認識機能はどんな画像でも`beer`と答えるようになっている｡
再生機能は本当に未実装｡
