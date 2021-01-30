import discord

bot = discord.Client()

@bot.event
def on_ready():
    print("prêt à fonctionner")

token = "ODA1MTUxNTgzMTk2NDEzOTY0.YBWt2A.zJOsKclt6ee4vMk2GxRmAH8hfLY"

bot.run(token)