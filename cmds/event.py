import discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime
with open('setting.json', mode='r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata['WELCOME']))
        embed=discord.Embed(title=f'**{member}** 加入!', url="https://cdn.discordapp.com/attachments/846756328520155206/974632470794342420/FB_IMG_1652318148320.jpg", description="進入請看規則喔", color=0x49e01f)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/846756328520155206/974632470794342420/FB_IMG_1652318148320.jpg")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['WELCOME']))
        embed=discord.Embed(title=f'{member} 離開!', url="https://cdn.discordapp.com/attachments/915252108507365386/974926085466779688/not_megumin_543330203_p_2836582481815224056_1_p_2836582481815224056.webp", description="後會有期", color=0xf10914)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915252108507365386/974926085466779688/not_megumin_543330203_p_2836582481815224056_1_p_2836582481815224056.webp")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content =='早上好':
            await msg.channel.send('中國')
            await msg.channel.send('現在我有冰淇淋')
        if msg.content =='晚上好':
            await msg.channel.send('嗨~ 消夜吃了嗎')
        if msg.content =='我好孤單':
            await msg.channel.send('不管你需不需要，我一直都在。')
        if msg.content =='兩個禮拜以後':
            await msg.channel.send('速度與激情9~')
        if msg.content =='搞笑影片':
            await msg.channel.send('||https://www.youtube.com/watch?v=BjDebmqFRuc&list=LL&index=64&ab_channel=MrMeme||')
        if msg.content=='晚安':
            await msg.channel.send('晚安~')
        if msg.content =='阿寬':
            await msg.channel.send('@579231390449795093')
        if msg.content =='我太難了':
            await msg.channel.send('拍拍')
        if msg.content =='鄧福如':
            await msg.channel.send('叉子勒')
        if msg.content =='一路發':
            await msg.channel.send('Q~~~~~~')
        if msg.content =='隔離7天':
            await msg.channel.send('168小時')
        if msg.content =='昨天早上吃完早餐':
            await msg.channel.send('突然好想吃芭樂')
        elif msg.content == '寬':
            await msg.channel.send('<@579231390449795093>')
        elif msg.content == '大會報告':
            await msg.channel.send('@everyone')
        elif msg.content == '打瓦':
            await msg.channel.send('<@&975574886078619738>')
        elif msg.content == '打apex':
            await msg.channel.send('<@&975581060412882965>')
        elif msg.content == '上課了':
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
        if msg.content =='電子學實習電路網址':
            await msg.channel.send('http://www.falstad.com/circuit/circuitjs.html')
        elif msg.content == '傑克':
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
            await msg.channel.send('<@696170463302254663>')
        if msg.content =='體育網址':
            await msg.channel.send(' https://drive.google.com/drive/folders/1eJM_eHsSECtu6bCRC0FJfSdd4ZHvNG5V')
        if msg.content =='國文網址':
            await msg.channel.send('  https://meet.google.com/wqn-qaie-qmh')

    
       
        

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #https://youtu.be/ojSb06_jm9Y?list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&t=2727
        if hasattr(ctx.command,'on_error'):
            return

        if isinstance(error,commands.errors.MissingRequiredArgument):
            embed=discord.Embed(title="↓↓↓↓↓↓")
            embed.set_author(name="🛑錯誤指令🛑")
            embed.add_field(name="請輸入正確參數", value="查詢指令k! helpp", inline=False)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.CommandNotFound):
            embed=discord.Embed(title="↓↓↓↓↓↓")
            embed.set_author(name="🛑錯誤指令🛑")
            embed.add_field(name="請輸入正確指令", value="查詢指令k! helpp", inline=False)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="↓↓↓↓↓↓")
            embed.set_author(name="🛑錯誤指令🛑")
            embed.add_field(name=" 發生錯誤", value="請@阿寬處理", inline=False)
            await ctx.send(embed=embed)

  

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,reaction,user):
        print(reaction)
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id ==993335821723779123:
            if str(payload.emoji) == '<:emoji_55:984607094198132757>':
                guild = self.bot.get_guild(payload.guild_id)
                role = guild.get_role(993163539030220900)
                await payload.member.add_roles(role)
                embed=discord.Embed(title=f"已新增 {role} 身分組",color=0x4dff00, timestamp = datetime.datetime.now())
                embed.set_author(name="身分組領取通知")
                await payload.member.send(embed = embed)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id ==993335821723779123:
            if str(payload.emoji) == '<:emoji_55:984607094198132757>':
                guild = self.bot.get_guild(payload.guild_id)
                user = guild.get_member(payload.user_id)
                role = guild.get_role(993163539030220900)
                await user.remove_roles(role)
                embed=discord.Embed(title=f"已移除 {role} 身分組",color=0xf40101, timestamp = datetime.datetime.now())
                embed.set_author(name="身分組移除通知")
                await user.send(embed = embed)    
        
def setup(bot):
    bot.add_cog(event(bot)) 