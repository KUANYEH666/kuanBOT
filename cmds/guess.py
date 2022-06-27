from ast import Num
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import datetime

with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)


class guess(Cog_Extension):
    # @commands.command()
    # async def guess(self, ctx):
    
    # # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
    #     def check(number):
    #         return number.author == ctx.author and number.channel == ctx.message.channel
    #     global lowernumber
    #     global highernumber
    
    #     lowernumber = 1
    #     highernumber = 100
    
    #     number = random.randint(lowernumber, highernumber)
    #     print(number)
    # # print(number)
    
    #     embed=discord.Embed(title="終極密碼")
    #     embed.set_author(name="歡迎遊玩終極密碼", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
    #     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
    #     embed.add_field(name="請輸入", value="1~100中的數字", inline=False)
    #     await ctx.send(embed=embed)


    #     for i in range(10):    
    #         response = await self.bot.wait_for('message', check = check)
        
    #         try : 
    #             guess = int(response.content) 

        
    #         except:
    #             embed=discord.Embed(title="e04")
    #             embed.set_author(name="🛑錯誤!🛑")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
    #             embed.add_field(name="不會玩終極密碼逆", value="輸入數字拉幹", inline=False)
    #             await ctx.send(embed=embed)
            
    #         if guess == number : 
    #             embed=discord.Embed(title="恭喜你")
    #             embed.set_author(name="答對拉~", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815090351759450/congratulations.gif")
    #             embed.add_field(name="正確", value=f'答案就是{number}', inline=False)
    #             await ctx.send(embed=embed)
    #             break
            
    #         if guess > 100 :
    #             embed=discord.Embed(title="e04")
    #             embed.set_author(name="🛑錯誤!🛑")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
    #             embed.add_field(name="不會玩終極密碼逆", value="大於100", inline=False)
    #             await ctx.send(embed=embed)

    #         if guess < 1 :
    #             embed=discord.Embed(title="e04")
    #             embed.set_author(name="🛑錯誤!🛑")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
    #             embed.add_field(name="不會玩終極密碼逆", value="小於1", inline=False)
    #             await ctx.send(embed=embed)
            
    #         if 0 < guess < number:
    #             lowernumber = guess
    #             embed=discord.Embed(title="終極密碼")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
    #             embed.add_field(name="請繼續", value="", inline=False)
    #             embed.add_field(name=f'比{lowernumber}大比{highernumber}小', value="加油", inline=False)
    #             await ctx.send(embed=embed)

    #         if 101 > guess > number :
    #             highernumber = guess
    #             embed=discord.Embed(title="終極密碼")
    #             embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
    #             embed.add_field(name="請繼續", value="", inline=False)
    #             embed.add_field(name=f'比{lowernumber}大比{highernumber}小', value="加油", inline=False)
    #             await ctx.send(embed=embed)
    #     else:
    #         embed=discord.Embed(title="差一點")
    #         embed.set_author(name="GG", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
    #         embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815090351759450/congratulations.gif")
    #         embed.add_field(name="可惜", value=f"答案是{number}", inline=False)
    #         await ctx.send(embed=embed)

    @commands.command()
    async def ab(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.message.channel
        embed=discord.Embed(title="1A2B小遊戲", description="請輸入4個不重複數字，喔對了你只要沒打4個數字我會自己重來", timestamp = datetime.datetime.utcnow())
        embed.set_author(name="遊戲", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/980642315385307156/Screenshot_2022-05-30-09-22-14-869_com.miui.mediaeditor.png")
        await ctx.send(embed=embed)
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
            # try:
            #     i[int:Num]
    
            # except:
            #     embed=discord.Embed(title="🤔 ‖ 請輸入數字", color=0xff0000, timestamp = datetime.datetime.now())
            #     embed.set_author(name="🕹️ 娛樂中心 🕹️")
            #     embed.set_thumbnail(url="https://cdn.dribbble.com/users/648258/screenshots/9070602/media/20cef9101ef2a1f1617b6b020ec97157.gif")
            #     await ctx.send(ctx.author.mention,embed=embed)
            for i in range(4):
                for j in range(4):
                    if ans[i] == ab[j] and i == j:
                            a += 1
                    if ans[i] == ab[j] and i != j:
                            b += 1
            if a != 4:
                embed=discord.Embed(title="1A2B小遊戲")
                embed.set_author(name="遊戲", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/980642315385307156/Screenshot_2022-05-30-09-22-14-869_com.miui.mediaeditor.png")
                embed.add_field(name=f"第{times}次", value=f"`{a}` A`{b}` B", inline=False)
                await ctx.send(embed=embed)
                
            if a == 4:
                embed=discord.Embed(title="1A2B小遊戲")
                embed.set_author(name="遊戲", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/980642315385307156/Screenshot_2022-05-30-09-22-14-869_com.miui.mediaeditor.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815090351759450/congratulations.gif")
                embed.add_field(name="恭喜你答對了", value=f"花了{times}次", inline=False)
                await ctx.send(embed=embed)
                break

            guess = await self.bot.wait_for("message",check = check)
            guess = guess.content
            ab = [int(i) for i in guess]
            a = 0
            b = 0
            times += 1
            if times > 10:
                embed=discord.Embed(title="1A2B小遊戲")
                embed.set_author(name="遊戲", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/980642315385307156/Screenshot_2022-05-30-09-22-14-869_com.miui.mediaeditor.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815897323274250/e52430e7f1d106372201c951d38c982a.gif")
                embed.add_field(name="可惜阿", value="你失敗了", inline=False)
                embed.add_field(name="答案是", value=f"{ans}", inline=True)
                await ctx.send(embed=embed)
                break
    @ab.error
    async def command_ab_error(self,ctx,error:str):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'error')
   
            
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
        print(number)
    # print(number)
    
        embed=discord.Embed(title="終極密碼")
        embed.set_author(name="歡迎遊玩終極密碼", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
        embed.add_field(name="請輸入", value="1~100中的數字", inline=False)
        await ctx.send(embed=embed)


        for i in range(10):    
            response = await self.bot.wait_for('message', check = check)
        
            try : 
                guess = int(response.content) 

        
            except:
                embed=discord.Embed(title="e04")
                embed.set_author(name="🛑錯誤!🛑")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
                embed.add_field(name="不會玩終極密碼逆", value="輸入數字拉幹", inline=False)
                await ctx.send(embed=embed)
            
            if guess == number : 
                embed=discord.Embed(title="恭喜你")
                embed.set_author(name="答對拉~", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815090351759450/congratulations.gif")
                embed.add_field(name="正確", value=f'答案就是{number}', inline=False)
                await ctx.send(embed=embed)
                break
            
            if guess > 100 :
                embed=discord.Embed(title="e04")
                embed.set_author(name="🛑錯誤!🛑")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
                embed.add_field(name="不會玩終極密碼逆", value="大於100", inline=False)
                await ctx.send(embed=embed)

            if guess < 1 :
                embed=discord.Embed(title="e04")
                embed.set_author(name="🛑錯誤!🛑")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981746032583012372/9936c1bd85ee255b5d8adad1fb2f5c95.gif")
                embed.add_field(name="不會玩終極密碼逆", value="小於1", inline=False)
                await ctx.send(embed=embed)
            
            if 0 < guess < number:
                lowernumber = guess
                embed=discord.Embed(title="終極密碼")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
                embed.add_field(name="請繼續", value="", inline=False)
                embed.add_field(name=f'比{lowernumber}大比{highernumber}小', value="加油", inline=False)
                await ctx.send(embed=embed)

            if 101 > guess > number :
                embed=discord.Embed(title="終極密碼")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/981434436367310939/hololive_vtuber_art_543811126_p_2849634115790321129_1_p_2849634115790321129.webp")
                embed.add_field(name="請繼續", value="", inline=False)
                embed.add_field(name=f'比{lowernumber}大比{highernumber}小', value="加油", inline=False)
                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="差一點")
            embed.set_author(name="GG", icon_url="https://cdn.discordapp.com/attachments/915252108507365386/981748316213760040/1654137429311.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/980815090351759450/congratulations.gif")
            embed.add_field(name="可惜", value=f"答案是{number}", inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(guess(bot))