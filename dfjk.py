import discord
import asyncio
import os


client = discord.Client()

@client.event
async def on_ready():
    print("hi")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="{} SERVER | {} USER". format(len(client.guilds), len(client.users))))


@client.event
async def on_message(message):
    if message.content.startswith("/회원가입'):
                                  await message.channel.send("권한을 발급합니다.")
                                  author = message.guild.get_member(int(message.author.id))
                                  role = discord.utils.get(message.guild.roles, name="회원")
                                  await author.add_roles(role)
                                  role = discord.utils.get(message.guild.roles, name="비회원")
                                  await author.remove_roles(role)
    

    



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
