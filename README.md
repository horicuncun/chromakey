# chromakey
Webカメラで撮影した映像にクロマキー合成を行うプログラム。

# 必要なもの
+ Webカメラ
+ python3
+ numpy
+ cv2

# 使い方
1. WebカメラをPCに接続
1. cd chromakey
1. python camera.py （実行後、映像が表示されます)
1. 撮影が終わったら、映像をクリックし、キーボードのqを押下<br>
(./movie_originalに合成前の動画が、　./movie_chromakeyに合成後の動画が保存されます。)

# うまくいかないときは
+ lower_color、uppder_colorでHSV空間に基づいた緑色の閾値を設定しています。緑色の検知がうまくいかないときは、ここの値を変えるといいと思います。
