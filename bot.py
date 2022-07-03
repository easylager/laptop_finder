import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token, chat_id
import asyncio
from bs4 import BeautifulSoup
import requests
from models import Laptop
import time
from seleniumrequests import Firefox



bot = Bot(token='5578582382:AAEwTFDUjaV2Rk1i9PVqJq-KE6WrSoAGAnM', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

kufar_url = 'https://www.kufar.by'
headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding':  'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'www.kufar.by',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }
params = {'Scheme': 'https',
          'Host': 'www.kufar.by',
          'Filename': '/l/noutbuki',
          'ot': '1',
          'query': 'ноутбук',
          'rgn': 'all',
        }

async def news_every_minute():
    while True:

        # Simple usage with built-in WebDrivers:
        
        soup = BeautifulSoup(res.text, 'lxml')

        list_of_items = soup.find('div', {"data-name": "listings"})

        items = list_of_items.find_all('section')
        n = 0
        print(type(list(items)))
        for item in items:
            link = item.find('a').get('href')
            hash = link.split('/')[-1]
            print(f'{hash}:{link}')
            n += 1
        print(n)

        """if not Laptop.hash_exist(incoming_laptop_hash=hash):
            laptop = Laptop(hash, link)
            result = f'{laptop.link}'
            await bot.send_message('1304982166', result)"""

        await asyncio.sleep(random.randrange(30, 80))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Fresh tires', 'Models']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Let'start bussines" , reply_markup=keyboard)


"""@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")"""


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()