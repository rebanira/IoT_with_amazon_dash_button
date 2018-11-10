"""
ダッシュボタンが押されたときに呼び出される関数一覧
"""
import discord_bot

def send_to_discord():
    """
    discordに通知を送る関数
    """
    discord_bot.send_message("呼ばれているよ")