import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
from kuanbot import reload



class guess(Cog_Extension):
    @commands.command()
    async def guess(self, ctx):
        
        # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
        
        lowernumber = 1
        highernumber = 100
        
        number = random.randint(lowernumber, highernumber)
        # print(number)
        
        await ctx.send('1-100，任意選一個數字(10次機會)')
        
        for i in range(0, 10):    
            response = await self.bot.wait_for('message', check = check)
            
            try : 
                guess = int(response.content) 
            
            except:
                await ctx.send("請輸入數字")
                
            if guess > 100 :
                await ctx.send("超過100，格式錯誤")
                
            if guess < number:
                lowernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
                
            if guess > number :
                highernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")

            if guess == number : 
                await ctx.send("猜對了")
               
                break
        await ctx.send('10次機會已經用完了,請再次挑戰')

                    
def setup(bot):
    bot.add_cog(guess(bot))