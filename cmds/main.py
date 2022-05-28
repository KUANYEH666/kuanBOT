from dataclasses import dataclass
from http.client import ImproperConnectionState
from sqlite3 import Timestamp
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
from core import check
import json
with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)
class main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        embed=discord.Embed(title="延遲", color=0xec6f6f)
        embed.add_field(name=f"{round(self.bot.latency*1000)}", value=" (ms)", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def hi(self,ctx):
        await ctx.send("嗨")
    
    @commands.command()
    async def into(self,ctx):
        embed=discord.Embed(title="🔸機器人資料🔸 ", description="名字:𝒦𝒰𝒜𝒩-ℬ𝒪𝒯", color=0x4cad0b)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/974975272388526132/975301807846850610/6d815ed644790f6bf169586b50975e9c.jpg")
        embed.add_field(name="生日🎂：2022/5/14 ", value="作者:阿寬", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def helpp(self,ctx):
        embed=discord.Embed(title="指令",
        timestamp=datetime.datetime.now())
        embed.add_field(name="前面記得+k! ", value="記得喔", inline=True)
        embed.add_field(name="hi ", value="我會跟你說嗨", inline=False)
        embed.add_field(name="into", value="我的資訊", inline=False)
        embed.add_field(name="helpp", value="查詢", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        embed=discord.Embed(title="𝒞𝓁𝑒𝒶𝓃")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/975376378444787774/b5931bd82ea9b701e2ab2b70025d46ca.jpg")
        embed.add_field(name="刪除指令", value=f"我刪除了{num}條訊息", inline=False)
        await ctx.send(embed=embed)
    
  


    
    


     



def setup(bot):
    bot.add_cog(main(bot)) 
