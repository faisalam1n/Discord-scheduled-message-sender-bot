import discord
from discord.ext import tasks

client = discord.Client()
guild_id = 1234 # Enter your Server ID
channel_id = 1234 # Enter the ID of the channel you wanna send msg to
token = 'token' # Enter your Token here
message = "Hi" # Enter the msg you wanna send

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=30) # You can modify it to "seconds, minutes, hours, counts"
async def send():
    guild = client.get_guild(guild_id)
    if guild and guild.get_channel(channel_id):
        await guild.get_channel(channel_id).send(message) 
        print("Message Sent in {0}!!".format(guild.get_channel(channel_id)))

send.start()
client.run(token)
