import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!Arkiver"):
        archiveChannel =  message.content.split(' ')[0].split("!Arkiver")[1]
        print(archiveChannel)
        for channel in client.get_all_channels():
            if channel.name.startswith(archiveChannel):
                await client.send_message(channel, message.author.mention + " wrote:   " + message.content)

    if  client.user.mentioned_in(message):
        archiveChannel =""
        archiveChannel =  message.content.split(' ')[1]
        print(archiveChannel)
        for channel in client.get_all_channels():
            if channel.name.startswith(archiveChannel):
                await client.send_message(channel, message.author.mention + " wrote:   " + message.content)

client.run('Token')
