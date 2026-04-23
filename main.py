import discord
from discord.ext import commands
import os

# 기본 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 명령어 접두사 설정 (예: !hello)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'봇이 준비되었습니다: {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    """퐁을 응답하는 테스트 명령어입니다."""
    await ctx.send('pong!')

@bot.command()
async def hello(ctx):
    """인사하는 명령어입니다."""
    await ctx.send(f'안녕하세요, {ctx.author.name}님! 디스코드 봇 테스트 중입니다.')

if __name__ == "__main__":
    # 환경변수에서 디스코드 토큰을 가져옵니다. 
    # 로컬 테스트 시에는 '여기에_봇_토큰_입력' 부분을 실제 토큰으로 변경하거나 
    # 터미널에서 export DISCORD_BOT_TOKEN="내토큰" 을 입력하세요.
    TOKEN = os.environ.get('DISCORD_BOT_TOKEN', '여기에_봇_토큰_입력')
    
    if TOKEN and TOKEN != '여기에_봇_토큰_입력':
        bot.run(TOKEN)
    else:
        print("오류: 디스코드 봇 토큰이 설정되지 않았습니다.")
        print("os.environ.get 에 토큰을 입력하거나 DISCORD_BOT_TOKEN 환경변수를 설정해주세요.")
