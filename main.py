import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

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
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    if TOKEN and TOKEN != 'your_token_here':
        bot.run(TOKEN)
    else:
        print("오류: 디스코드 봇 토큰이 설정되지 않았습니다.")
        print(".env 파일에 DISCORD_BOT_TOKEN 값을 설정해주세요.")

# 이 코드는 디스코드 봇을 설정하고, 간단한 명령어를 추가하는 예제입니다.