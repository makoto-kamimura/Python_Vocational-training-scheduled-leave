# Python_Vocational-training-scheduled-leave
当ツールは厚生労働省求職者支援訓練制度における職業訓練校受講の際に、  
出席日数等の所定日程の計算を補助するツールとなります。  
ご利用の際には、本README下部に記載している Note をお読みの上ご利用ください。

# DEMO
※後程更新を予定
* Demo  
![Python_Vocational-training-scheduled-leave.gif](/README_img/Python_Vocational-training-scheduled-leave.gif)  
* Document  
![Python_Vocational-training-scheduled-leave.pdf](/README_img/Python_Vocational-training-scheduled-leave.pdf)  

# Installation
後程更新を予定
```bash
git clone https://github.com/makoto-kamimura/Python_Vocational-training-scheduled-leave.git
cd Docker/
docker-compose up -d --build
docker-compose exec python3 bash
python source/Vocational-training-scheduled-leave.py
exit
```

# Note
※1 訓練校毎に所定条件等がございますので、そちらをご確認の上のご利用をお願い致します。  
※2 本ツールは下記条件にて計算しておりますので、訓練校によっては所定条件と異なる場合がございますので予めご了承願います。  
* 出席すべき日数の8割を下回ると退校処分

# License
"Python_Vocational-training-scheduled-leave" is Confidential.
