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


## Files
### dj_glass.py
本体スクリプト
それぞれのクラスをimportしてスレッドをまわしている。
 
### camera.py
picameraクラスの定義.
このスクリプトを実行するとpicamera画像がプレビューできるスクリプトが実行されるようになってる。

### dummy_camera.py
picameraクラスと同じインターフェースでダミー画像が取得できるクラス。
picameraクラスのオブジェクトと同じように使える。
picameraの接続されていないPCなどでもDjGlassの動作確認をするためにしよう。
ラズパイでデバッグきびしい。。。。。

### drink_detect.py
画像を入力してドリンクの種類を推定するクラス。
**未実装**
```
        input: img (numpyarray int8 32*32)
        output: {'id': drink_id(int), 'name': drink_name(str)}
```

### img/
画像の保存場所。`sample.jpg`はDummyCameraで使用。


