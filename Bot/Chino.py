import logging
import os
import random

import discord
from discord.ext import commands, tasks

'''Logger設置'''
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix='$', owner_id=252029078452961280)

'''更改Bot狀態'''


@tasks.loop(minutes=1)
async def change_presence_task():
    await client.wait_until_ready()
    with open(os.path.join('.', 'Bot', 'data', 'statusList'), 'r', encoding='UTF-8') as f:
        l = f.readlines()

    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(l)))


@client.event
async def on_ready():
    logger.info('登入成功')
    logger.info(f'Bot名稱： {client.user.name}')
    logger.info('----------')


'''清除預設help指令'''
client.remove_command('help')
'''載入cog'''
logger.info('開始載入cogs')
for filename in os.listdir(os.path.join('.', 'Bot', 'cogs')):
    if filename.endswith('.py'):
        '''[:-3]去掉檔案的.py副檔名'''
        client.load_extension(f'cogs.{filename[:-3]}')
        logger.info(f'已載入{filename}')
logger.info('cogs載入完畢')
logger.info('----------')

'''啟動Loop Task'''
logger.info('啟動循環task')
change_presence_task.start()
logger.info('循環task啟動完畢')
logger.info('----------')

'''啟動程式上線'''
with open(os.path.join('.', 'Bot', 'data', 'token'), 'r', encoding='UTF-8') as f:
    token = f.readline()
'''啟動程式上線'''
client.run(token)
