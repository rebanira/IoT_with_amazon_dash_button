"""
ARPを検知してMACアドレスを読みとる
検知した中にダッシュボタンのMACアドレスがあった場合、ボタンに応じた処理をするプログラム
"""

from kamene.all import * # ARP検知用ライブラリ
import dash_button_list # ダッシュボタンのmacアドレスリスト
import dash_button_functions # ダッシュボタンに応じたモジュールまとめ

def call_function(pkt):
    """
    MACアドレスを読み取り対応するダッシュボタンの関数を呼び出す
    """
    if ARP in pkt and pkt[ARP].op in (1, 2):
        mac_address = pkt.sprintf("%ARP.hwsrc%")

        # ダッシュボタンのIDを取得、ボタンのIDでない場合は-1が返る
        dash_button = dash_button_detector(mac_address)

        # ボタンのIDごとに処理
        if dash_button == 0:
            print("DrPepper")
            # discordに通知
            dash_button_functions.send_to_discord()

def dash_button_detector(mac_address):
    """
    input:macアドレス
    output:ダッシュボタンのID
    """
    id = -1
    # ダッシュボタンのリストを取得
    db_mac_list = dash_button_list.mac_address

    # 引数に与えられたMACアドレスがリストにあるか確認
    # ある場合は配列の番号をIDにする
    for i in range(0, len(db_mac_list)):
        if mac_address == db_mac_list[i]:
            id = i
    
    return id

# ARP検知
sniff(prn=call_function, filter="arp", store=0)