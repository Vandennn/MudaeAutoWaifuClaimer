import discord
import json
import time

TOKEN = "TOKEN"

waifuList = [PUT YOUR WAIFUS HERE]
shitTalk = False #type True and add your quotes to the shitTalkList to shit talk after a claim (still buggy, will message multiple times, I still need to fix so I do not suggest using for now)
#change to true or false to add shit talking or not ^^
shitTalkList = [PUT QUOTES HERE]
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print('------')

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID_HERE and message.author.id == 432610292342587392 and message.embeds:
      embed = message.embeds[0].to_dict()
      embedVal = json.dumps(embed)
      print(embedVal)
      ##print(embedVal)
      for x in waifuList:
        if (x + '"') in embedVal and "Claim Rank" not in embedVal:
          await message.add_reaction("❤️")
          time.sleep(3)
          if shitTalk == True:
            for x in shitTalkList:
              await message.channel.send("Fuck yall pussy ass bitches")
              print("done")
client.run(TOKEN)


