# IoT with amazon dash button
- amazon dash buttonを使ったIoTをするコードです。
- ダッシュボタンを押したときにdiscordでBotが発言するサンプルコードが入っています。
- windowsで動作確認済み
# Requirement
- Python 3.6.x
- discord.py 0.16.12
- kamene 0.32

# Installation
- discord.py
```
$ pip3 install discord.py
```
- kamene
```
$ pip3 install kaneme
```

# Usage
- discordのBot設定
    - scripts/discors_bit.pyを編集
    ```
    7行目：channel = client.get_channel('[チャンネルのコード]')# 発言するチャンネルのコードを入力
    11行目：client.loop.run_until_complete(client.start('[サーバーのアクセスコード]')) #サーバーのアクセスコードを入力
    ```
- amazon dash buttonのMACアドレスの設定
    - scripts/dash_button_list.pyを編集
    ```
    #サンプルそのままではID0しか対応していません。
    mac_address = ["aa:aa:aa:aa:aa:aa", #id:0
                   "bb:bb:bb:bb:bb:bb"  #id:1
                            :
                            :
                            :         ] #id:n
    ```
- 動作確認
    - プログラム実行
    ```
    $ py detect_dash_button.py
    ```
    - ダッシュボタンを押して通知がこれば成功です。