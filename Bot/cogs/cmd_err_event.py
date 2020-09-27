import logging

from discord.ext import commands
from discord.ext.commands import *

'''Logger設置'''
logger = logging.getLogger('discord')
authorM = '<@252029078452961280>'


class CmdErrEvent(commands.Cog):

    def __init__(self, client):
        self.client = client

    # on_command_error事件
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''
        ignored
        CommandNotFound,MissingPermissions,MissingRequiredArgument,NoPrivateMessage
        '''

        if isinstance(error, CommandNotFound):
            return
        elif isinstance(error, BotMissingPermissions):
            await ctx.send('看來我是不被允許做這件事的...')
            return
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send('漏了一些細節嗎?')
            return
        elif isinstance(error, BadArgument):
            await ctx.send('無法理解...')
            return
        elif isinstance(error, NoPrivateMessage):
            await ctx.send('沒辦法在這邊做呢...')
            return
        elif isinstance(error, NotOwner):
            await ctx.send('你不被允許做這種事!')
            return
        raise error


def setup(client):
    client.add_cog(CmdErrEvent(client))
