from typing_extensions import Self
import discord 
from discord.ext import commands
import json
import os
with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='k!',intents=intents)

@bot.event
async def on_ready():
    print("}}機器人已上線{{")
    game = discord.Game('主人罷工，不想更新')
    await bot.change_presence(status=discord.Status.idle, activity=game)


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