import discord

def send_message(msg):
    client = discord.Client()
    @client.event
    async def on_ready():
        channel = client.get_channel('[チャンネルのコード]')
        await client.send_message(channel,msg)
        await client.logout()   

    client.loop.run_until_complete(client.start('[サーバーのアクセスコード]'))
