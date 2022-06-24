from typing_extensions import Self
import discord 
from discord.ext import commands
import json
import os
import random
import datetime
import asyncio
with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='k!',intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.idle,activity = discord.Game(name = "啟動中"))
    await bot.change_presence(status = discord.Status.online,activity = discord.Game(name = ">>機器人啟動完成<<"))
    print(">>機器人啟動完成<<")
async def ch_pr():
    await bot.wait_until_ready()
    bot.reload_extension('cmds.event')
    statuses = [f" 加入了{len(bot.guilds)}伺服器" , "查指令 ‖ k!helpp", "加入我的DC ==>https://discord.gg/sAVz7bjynC"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(status = discord.Status.dnd,activity = discord.Game(name = status))

        await asyncio.sleep(5)

bot.loop.create_task(ch_pr())

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    embed=discord.Embed(title="通知", description=f"**{extension}**資料夾成功讀取", color=0x4cad0b)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/975385518139379792/b7556a97bb97949ba011e9ea48241acb.jpg")
    await ctx.send(embed=embed) 
   
 
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    embed=discord.Embed(title="通知", description=f"**{extension}**資料夾成功移除", color=0x4cad0b)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/975385518139379792/b7556a97bb97949ba011e9ea48241acb.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    embed=discord.Embed(title="通知", description=f"**{extension}**資料夾重新讀取", color=0x4cad0b)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/975385518139379792/b7556a97bb97949ba011e9ea48241acb.jpg")
    await ctx.send(embed=embed)
    
@commands.command()
async def change(ctx,*,msg):
    await ctx.message.delete()
    game = await bot.wait_for("message")
    await bot.change_presence(status=discord.Status.idle, activity=game)



for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__=="__main__":
    bot.run(jdata['TOKEN'])