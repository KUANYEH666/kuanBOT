import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
async def get_bank_data():
    with open("bank.json", "r")as f:            
        users = json.load(f)
    return users

    
    

class daily(Cog_Extension):
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        pass
        await open_account(ctx.author)

        users = await get_bank_data()
        user = ctx.author
        earnings = random.randrange(3000)
        await ctx.send(f"簽到，你拿了 {earnings} 塊:yin_yang: ")
        users[str(user.id)]["wallet"] += earnings
        with open("bank.json", "w") as f:
            json.dump(users, f)
        money = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
        return money
  

    @daily.error
    async def command_daily_error(self,ctx,error:str):
        if isinstance(error, commands.CommandOnCooldown):
            cd = int(error.retry_after)
            H = int(cd / 3600)
            M = (int(cd / 60)- H*60)
            S = int(cd % 60)
            em = discord.Embed(title=f"北七喔!沒看到(簽到)逆",description=f"{H}小時{M}分{S}秒", color=0x4cad0b)
            await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(daily(bot)) 