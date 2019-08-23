import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("hi")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="{} SERVER | {} USER". format(len(client.guilds), len(client.users))))


@client.event
async def on_message(message):
    if message.content.startswith("/회원가입"):
        a = message.guild.get_member(int(message.author.id))
        b = discord.utils.get(message.guild.roles, name="회원")
        await a.add_roles(b)
        b = discord.utils.get(message.guild.roles, name="비회원")
        await a.remove_roles(role)
    

    



client.run("NjE0MDUwMDM5MTM1ODYyODI0.XV50sg.lGZAUA3TMQ244g9z9TYVH9pLnGk")
