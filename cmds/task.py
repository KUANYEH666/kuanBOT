
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

class task(Cog_Extension):
    def __init__(self,*args,**kwars):
        super().__init__(*args,**kwars)
    
        async def interval():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(976833870659977236)
            while not self.bot.is_closed():
                await self.channel.send('hi 我啟動了')
                await asyncio.sleep(5)
            
            self.bd_task=self.bot.loop.create_task(interval())

def setup (bot):
    bot.add_cog(task(bot))
