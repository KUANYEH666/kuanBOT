from dataclasses import dataclass
from http.client import ImproperConnectionState
from os import rename
from sqlite3 import Timestamp
import discord
import datetime
import random
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
        embed=discord.Embed(title="HELP", timestamp = datetime.datetime.utcnow())
        embed.set_author(name="指令大全", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/980642315385307156/Screenshot_2022-05-30-09-22-14-869_com.miui.mediaeditor.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980822451300737144/df9a610f418d1c2f0a282e5ec7947917.jpg")
        embed.add_field(name="k!helpp", value="你不會打怎麼叫得出來", inline=False)
        embed.add_field(name="k!clean (幾條訊息)", value="可以刪除訊息", inline=True)
        embed.add_field(name="k!covid", value="這是一個神奇的確診符號", inline=False)
        embed.add_field(name="k!hi", value="我會跟你說嗨", inline=True)
        embed.add_field(name="k!into", value="機器人資訊", inline=True)
        embed.add_field(name="k!ping", value="延遲", inline=True)
        embed.add_field(name="k!sayd (話)", value="我會說你寫的字(不要欺負窩)", inline=False)
        embed.add_field(name="k!午餐", value="幫你想午餐", inline=True)
        embed.add_field(name="k!晚餐", value="幫你想晚餐", inline=True)
        embed.add_field(name="k!ab", value="我會跟你玩1A2B", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        embed=discord.Embed(title="𝒞𝓁𝑒𝒶𝓃", timestamp = datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/975376378444787774/b5931bd82ea9b701e2ab2b70025d46ca.jpg")
        embed.add_field(name="刪除指令", value=f"我刪除了{num}條訊息", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def 午餐(self,ctx):
        a = 1
        b = 11
        ans = random.randint(a,b)
        if ans == 1 :
            await ctx.send("滷肉飯")
        if ans == 2 :
            await ctx.send("咖哩飯")
        if ans == 3 :
            await ctx.send("煎餃")
        if ans == 4 :
            await ctx.send("買當勞")
        if ans == 5 :
            await ctx.send("ㄔㄐㄐ")
        if ans == 6 :
            await ctx.send("bang當")
        if ans == 7 :
            await ctx.send("7-11")
        if ans == 8 :
            await ctx.send("滷味")
        if ans == 9 :
            await ctx.send("珍奶配雞排")
        if ans == 10 :
            await ctx.send("牛肉麵")
        if ans == 11 :
            await ctx.send("榨菜肉絲麵")
    @午餐.error
    async def command_午餐_error(self,ctx,error:str):
        if isinstance(error, commands.CommandOnCooldown):
            cd = int(error.retry_after)
            await ctx.send(f'冷卻: 你還有{cd}秒')
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def 晚餐(self,ctx):
    
      
        a = 1
        b = 22
        ans = random.randint(a,b)
        for i in range(10):
            
            if ans == 1 :
                await ctx.send("滷肉飯")
            if ans == 2 :
                await ctx.send("咖哩飯")
            if ans == 3 :
                await ctx.send("牛丼")
            if ans == 4 :
                await ctx.send("買當勞")
            if ans == 5 :
                await ctx.send("ㄔㄐㄐ")
            if ans == 6 :
                await ctx.send("bang當")
            if ans == 7 :
                await ctx.send("7-11")
            if ans == 8 :
                await ctx.send("滷味")
            if ans == 9 :
                await ctx.send("珍奶配雞排")
            if ans == 10 :
                await ctx.send("牛肉麵")
            if ans == 11 :
                await ctx.send("榨菜肉絲麵")
            if ans == 12 :
                await ctx.send(f'甲賽')
                await ctx.send(":wc:  ")
            if ans == 13 :
                await ctx.send("感丼")
            if ans == 14 :
                await ctx.send("飯捲")
            if ans == 16 :
                await ctx.send("餛飩麵")
            if ans == 17 :
                await ctx.send("拉麵")
            if ans == 18 :
                await ctx.send("火鍋")
            if ans == 19 :
                await ctx.send("壽司")
            if ans == 20 :
                await ctx.send("肯雞雞")
            if ans == 21 :
                await ctx.send("鐵板麵")
            if ans == 22 :
                await ctx.send("炒飯")
   



    @晚餐.error
    async def command_晚餐_error(self,ctx,error:str):
        if isinstance(error, commands.CommandOnCooldown):
            cd = int(error.retry_after)
            await ctx.send(f'冷卻: 你還有{cd}秒')
       
    @commands.command()
    async def 晚(self,ctx):
       ans= random(jdata['dinner'])
       await ctx.send(f'{ans}')    
           


    @commands.command()
    async def covid(self,ctx):
        await ctx.send("╒═══════════════════════╕\n│ COVID-19          C         T                            │\n│                       ┌──────┐      ┌─┐        │\n")
        await ctx.send("│                      ▕     ❗  ❗ ▕       │    │       │\n│                       └──────┘       └─┘       │\n╘═══════════════════════╛")

    # @commands.command()
    # async def change(self, ctx):
    #     def check(msg):
    #         tmp = msg.content.split(" ",2)
    #         return msg.author == ctx.author and msg.channel == ctx.message.channel
            
    #     await ctx.send("改成啥")  
        
    #     game = await self.bot.wait_for("message",check = check)
    #     game = discord.Game(tmp[1])
    #     await self.bot.change_presence(status=discord.Status.idle, activity=game)
    @commands.command()
    async def 快篩(self,ctx):
        i = 1
        j = 2
        ans = random.randint(i,j)
        if ans == 1:
            await ctx.send("╒═══════════════════════╕\n│ COVID-19          C         T                            │\n│                       ┌──────┐      ┌─┐        │\n│                      ▕     ❗  ❗ ▕       │    │       │\n│                       └──────┘       └─┘       │\n╘═══════════════════════╛")
            
        if ans == 2:
            await ctx.send("╒═══════════════════════╕\n│ COVID-19          C         T                            │\n│                       ┌──────┐      ┌─┐        │\n│                      ▕     ❗        ▕       │    │       │\n│                       └──────┘       └─┘       │\n╘═══════════════════════╛")
                            
        
                            
  

    @commands.command()
    async def avatar(self, ctx, user : discord.Member):
        embed = discord.Embed(
            title = f"{user.name} 的頭像",
            color = user.color,
            timestamp = datetime.datetime.now()
        )
        embed.set_image(url = user.avatar)
        await ctx.reply(mention_author = False, embed = embed)
        


def setup(bot):
    bot.add_cog(main(bot)) 
