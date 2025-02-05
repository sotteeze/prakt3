import discord
from discord.ext import commands
import random

TOKEN = 'MTMzNjgwNzQ3ODQ3NzcxNzY3NQ.G3QVfE.te8xuqpgbDTj9heZr5_E9oU_0I7RFd5I67bD3w'

bot = commands.Bot(command_prefix="!")

image_urls = [
    "https://konivjab.net/wp-content/uploads/2021/06/programuju-v-pitoni.jpg",
    "https://apostrophe.ua/uploads/image/094a52a4f8755e35b1ad5b8f67b66c8c.jpg",
    "https://static.tengrinews.kz/userdata/news/2024/news_555280/thumb_b/photo_494419.jpeg",
]

@bot.command(name="pic")
async def send_pic(ctx):
    image_url = random.choice(image_urls)
    await ctx.send(image_url)

bot.run(TOKEN)