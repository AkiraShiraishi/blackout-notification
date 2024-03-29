# 低価格、8ステップでできる汎用停電アラート

## 概要
コンセントの停電を検知してLINE（グループも可）に通知します．専用機器を用意するよりもシンプルで安いです．実験器具や観測機器（生物、化学、物理等）の停電通知にご利用ください．

## 原理
Raspberry Piの入力機能を使って停電を検知します．Raspberry PiにAC100Vは直接入力できないので、ACアダプターとUSBケーブルを使って電圧を落として（＆DCに変換）から商用電源を入力します．Raspberry Piに入る電圧がだいたい3Vを下回ると停電と判断されます．

## 用意するもの
* （Raspberry Piが接続できるディスプレイやキーボード、マウスなどはあるものとします．また、Raspberry Piはインターネットに接続してください）  
* （基本的に稼働用と検出用でコンセントを２つ使用します．２つ空きがない場合は電源タップなどを用意してください）  
* Raspberry Pi Model 3または4  
* パススルー型モバイルバッテリー（充電と給電が同時にできるやつ）  
* AC100V-USBアダプターとUSBケーブル（100均などの安いやつでいい）  
* 適当な線 2本  （USB↔ラズパイ間を接続）
* カッターナイフ  
* LINEアカウント  

## ステップ
１．Raspberry Pi自体が停電の影響を受けないようにモバイルバッテリーを通して給電します．モバイルバッテリーを常時コンセントに繋いで充電しながら、Raspberry Piをモバイルバッテリーに繋いで動かします．  

２．USBケーブルの片方を切断し、導線２本を出して被覆をむきます．複数本あったら赤と黒を選んでください．被覆をむいた線と「適当な線」をつなぎます．接続部は熱収縮チューブまたは適当なテープなどで保護しておいてください．電圧は高くないのでそこまで強力に保護しなくても耐えます．  

４．線をラズパイの端子につなぎます．ラズパイをUSBポートが右に来るように置いたとき、赤い線は上の段の左から7番目、黒い線は8番目の端子につなぎます．USBケーブルの反対側をACアダプターに繋いだら、ハードウェアは完成です．  

５．LINE Notifyのトークンを取得します．「 https://notify-bot.line.me/ja/ 」に移動してLINE IDでログインします．ログインしたら、「マイページ」→「トークンを発行」の順に操作します．次の画面で「トークン名」には適当な名前を入力します．その後、１対１で通知を受け取る場合はそれを、グループに通知したい場合は送るグループを選択します．トークンが表示されるので、コピーします．  

６．（グループに通知する場合は、LINE Notifyをグループに招待します．）  

７．このリポジトリから「main.py」をダウンロードしてラズパイに移動し、１箇所だけ編集します．12行目に取得したトークンを貼り付けます．  

８．ACアダプターをコンセントに挿して、main.pyを実行します．Raspberry Piにある「Thonny」というソフトで実行します．コンソールに「正常監視中」と表示されるはずです．ACアダプターを抜く（停電を再現する）と、「停電が発生しています．速やかに対処してください．」というメッセージに変わり、同じものがLINEに送信されます．  

## おまけ
* 大抵のACアダプターは中にコンデンサーが入っていて、停電しても数秒間はRaspberry Piに電圧が出力され続けるため、停電後すぐに通知されないことがあります．  
* 停電時の通知間隔を変更できます．main.pyの39行目に設定値があります．単位は秒です．デフォルトでは600（10分）になっていて、停電が発生した場合、復旧（または手動でプログラムを停止）するまでの間、10分間隔でLINEに通知し続けます．  
