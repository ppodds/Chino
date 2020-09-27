import logging
from datetime import datetime, timedelta

import discord
from discord.ext import commands

'''Logger設置'''
logger = logging.getLogger('discord')
authorM = '<@252029078452961280>'
tibi = '<:tibi:759676593035018330>'


class BasicCmd(commands.Cog):

    def __init__(self, client):
        self.client = client

    '''
    ctx後的參數皆為指令參數
    (*,n)會把*後面所有字串當成n參數
    '''

    # 觀看Help
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(description="「現在我能做的事情不多呢...」")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.colour = 0x3dd1db
        embed.add_field(name=f'{tibi} {tibi} {tibi} 指令清單 {tibi} {tibi} {tibi}',
                        value='----------------------------------------------------------', inline=False)
        embed.add_field(name='help', value='指令說明', inline=False)
        embed.add_field(name='check　[統計天數]　[ASC/DESC(可選)]', value='統計近期的emoji使用次數，不輸入參數預設由小排到大', inline=False)
        embed.set_footer(text="由ppodds親手調教",
                         icon_url='https://cdn.discordapp.com/avatars/252029078452961280/551ebcf0c6e6a3807c54afef6d70a04c.png?size=1024')
        await ctx.send(embed=embed)

    # 觀看emoji使用頻率
    @commands.guild_only()
    @commands.command()
    async def check(self, ctx, search_range: int, order='ASC'):
        if not (order == 'ASC' or order == 'DESC'):
            return await ctx.send('排序只有ASC和DESC可以選!')
        if order == 'DESC':
            reverse = True
        else:
            reverse = False
        emojis = ctx.guild.emojis
        channels = ctx.guild.text_channels
        count = await cal_emoji(channels, emojis, search_range)

        # 輸出統計
        embed = discord.Embed(description=f"「下面是我統計的結果! 欸嘿嘿~{tibi}」")
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.colour = 0x3dd1db
        embed.description = ''
        # 抽出資料以進行排序
        items = count.items()
        # 排序
        result = sorted(items, key=lambda x: x[1], reverse=reverse)
        for item in result:
            for emoji in emojis:
                if emoji.name == item[0]:
                    embed.description += f'{emoji_out(emoji)}使用{item[1]}次\n'
                    break
        embed.set_footer(text="由ppodds親手調教",
                         icon_url='https://cdn.discordapp.com/avatars/252029078452961280/551ebcf0c6e6a3807c54afef6d70a04c.png?size=1024')
        await ctx.send(embed=embed)


async def cal_emoji(channels, emojis, search_range):
    # 用來儲存emoji的統計數目
    # emoji_name(string) -> count(int)
    count = {}
    # 初始化計數表
    for emoji in emojis:
        count[emoji.name] = 0
    # 統計頻道歷史中的emoji出現次數
    for channel in channels:
        async for message in channel.history(limit=None, after=datetime.now() - timedelta(days=search_range)):
            for emoji in emojis:
                if f':{emoji.name}:' in message.content:
                    count[emoji.name] += 1
    return count


def emoji_out(emoji):
    return f'<:{emoji.name}:{emoji.id}>'


def setup(client):
    client.add_cog(BasicCmd(client))
