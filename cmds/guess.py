import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)


class guess(Cog_Extension):
    @commands.command()
    async def ab(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.message.channel
        await ctx.message.delete()
        await ctx.send("請輸入4個不重複數字")
        A = [1,2,3,4,5,6,7,8,9]
        ans = random.sample(A,4)
        print(ans)
        guess = await self.bot.wait_for("message",check = check)
        guess = guess.content
        ab = [int(i) for i in guess]
        a = 0
        b = 0
        times = 1
        while 1 == 1:
            
            for i in range(4):
                for j in range(4):
                    if ans[i] == ab[j] and i == j:
                            a += 1
                    if ans[i] == ab[j] and i != j:
                            b += 1
            if a != 4:
                await ctx.send(f"`{a}` A`{b}` B, 猜了`{times}`次")
            if a == 4:
                await ctx.send(f"你答對拉~答案就是{guess}")
                break

            guess = await self.bot.wait_for("message",check = check)
            guess = guess.content
            ab = [int(i) for i in guess]
            a = 0
            b = 0
            times += 1
            if times == 10:
                await ctx.send(f"可惜你沒有猜出來~答案就是{ans}")
                break


def setup(bot):
    bot.add_cog(guess(bot))