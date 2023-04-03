#必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート
import sys                          #sysモジュールをインポート

import datetime
import requests

#LINE Notify setup
def send_message(gomi_type):
    url = "https://notify-api.line.me/api/notify" 
    token = "＜LINE Notifyで取得したトークンを入力＞"
    headers = {"Authorization" : "Bearer "+ token}
    message =  ("停電が発生しています．速やかに対処して下さい．")
    payload = {"message" : message} 
    r = requests.post(url, headers = headers, params=payload)


#ポート番号の定義
Sw_pin = 23                         #変数"Sw_pin"に23を格納

#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
#GPIO23を入力モードに設定してプルダウン抵抗を有効にする
GPIO.setup(Sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#while文で無限ループ
message = "停電が発生しています．速やかに対処して下さい．"
#GPIO23の入力を読み取る
while True:
    try:
        print(GPIO.input(Sw_pin))           #GPIO23が「ONで"1"」「OFFで"0"」
        
        if GPIO.input(Sw_pin) == 0:
            print("停電が発生しています．速やかに対処して下さい．")
            send_message(message)
        else:
            print("正常監視中")
        time.sleep(600)                     #数字の間隔で停電通知を繰り返します（単位：秒）

    except KeyboardInterrupt:               #Ctrl+Cキーが押された
        GPIO.cleanup()                      #GPIOをクリーンアップ
        sys.exit()                          #プログラムを終了
        
