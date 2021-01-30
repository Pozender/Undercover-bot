import discord

bot = discord.Client()

@bot.event
def on_ready():
    print("prêt à fonctionner")
  

token = "TOKEN"

bot.run(token)
