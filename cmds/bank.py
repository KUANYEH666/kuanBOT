import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio

async def update_bank(user, change = 0, mode = "wallet"):
    pass
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    money = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
    return money


async def open_account(user):
    pass
async def get_bank_data():
    pass
async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)
        
    return True

async def get_bank_data():
    with open("bank.json", "r")as f:            
        users = json.load(f)
    return users

shop = [
            {"name": "阿寬女裝", "price": 1000000000000},
            {"name": "傑克是渣男", "price": 87},
            {"name": "PC", "price": 870},
            {"name": "PS5", "price": 690},
            {"name": "Cat", "price": 1000}
        
        ]


class bank(Cog_Extension):

    @commands.command()
    async def money(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet = users[str(user.id)]["wallet"]
        bank = users[str(user.id)]["bank"]

        embed=discord.Embed(title="成員", description=f"{ctx.author.name}", color=0x5fecea)
        embed.set_thumbnail(url = user.avatar_url)
        embed.set_author(name="財產")
        embed.add_field(name="錢包",value = wallet,inline=False)
        embed.add_field(name="銀行",value = bank,inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def market(self, ctx):
        pass
        embed=discord.Embed(title="以下為貨品", color=0xab6bd6)
        embed.set_author(name="商店")
        
        for item in shop:
            name = item["name"]
            price = item["price"]
            embed.add_field(name = name, value = f"${price}")
        await ctx.send(embed=embed)
    @commands.command()
    async def beg(self, ctx):
        pass
        await open_account(ctx.author)
    
        users = await get_bank_data()
        user = ctx.author
        earnings = random.randrange(101)
        await ctx.send(f"某人給了你 {earnings} 塊錢!!")
        users[str(user.id)]["wallet"] += earnings
        with open("bank.json", "w") as f:
            json.dump(users, f)

        
        
        
    @commands.command()
    async def slots(self, ctx, amount = None, mang = None):
        pass
    
        await open_account(ctx.author)
        if mang == None:
            await ctx.send("請輸入倍率")
            return 
        bal = await update_bank(ctx.author)
        amount = int(amount)
        mang = int(mang)
        if bal[0] <= 0:
            await ctx.send("你啥都沒有")
            return 
        if amount > bal[0]:
            await ctx.send("你沒這麼多錢拉幹")
            return
        if amount < 0:
            await ctx.send("正整數...")
            return
        # 做出限制
        if amount > 200 or mang > 10 :
            await ctx.send("不接受太高金額及倍率，最高為199$$") 
            return
        final = []
        for i in range(3):
            a = random.choice(["X", "O", "Q"])
            final.append(a)
        ans = mang * amount
        pos = mang * amount * -1
        # win
        if final[0] == final[1] == final[2]:
            await update_bank(ctx.author, ans)
            await ctx.send("想贏嗎??")
            asyncio.sleep(3)
            await ctx.send(str(final))
            await ctx.send(f"你贏了 {ans} 塊錢")
        # lose
        else:
            await update_bank(ctx.author, pos)
            await ctx.send("想贏嗎??")
            asyncio.sleep(3)
            await ctx.send(str(final))
            await ctx.send(f"你輸了 {pos} 塊錢")

    @commands.command()
    async def bank_in(self, ctx, amount = None):   
        pass
        await open_account(ctx.author)
        if amount == None:
            await ctx.send("請輸入數字")
            return 
    async def update_bank(user, change = 0, mode = "wallet"):
        pass
        users = await get_bank_data()
        users[str(user.id)][mode] += change
        with open("bank.json", "w") as f:
            json.dump(users, f)
        bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]    
        return bal
        



















def setup(bot):
    bot.add_cog(bank(bot)) 


      

