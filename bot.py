import random
import asyncio
import requests
import urllib3
import re


from enum import Enum
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config.config_kufar import token, chat_id, name

from models.laptop import Laptop
from config.enums.enums import Goods
from parsers.response_constructor import ResponseConstructor
from parsers.advert_parser import AdvertParser
from handlers.config_handlers import (
    ProxiesHandler,
    UserAgentsHandler
)


bot = Bot(token='5578582382:AAEwTFDUjaV2Rk1i9PVqJq-KE6WrSoAGAnM', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)


async def news_every_minute():
    while True:
        http_manager = urllib3.PoolManager()
        response = http_manager.request(
            'GET',
            'https://www.kufar.by/l/r~minsk/noutbuki?clp=v.or%3A3%2C5%2C1&ot=0&prc=r%3A0%2C30000&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d'
        )
        """ response_req = requests.get(
            Goods.LAPTOPS,
            headers=UserAgentsHandler.header(),
            proxies=ProxiesHandler.proxy()
        )"""

        bs_object = BeautifulSoup(response.data, 'lxml')

        list_of_items = bs_object.find('div', {"data-name": "listings"})

        items = list_of_items.find_all('section')

        for item in items:
            link = item.find('a').get('href')
            hash = link.split('/')[-1]

            parser_object = AdvertParser(url=link)
            constructor_object = ResponseConstructor(parser=parser_object)

            print(f'{hash}:{link}')

            if not Laptop.hash_exist(incoming_laptop_hash=hash):
                laptop = Laptop(hash, link)
                result = f'{laptop.link}'
                await bot.send_message('1304982166', constructor_object.build_response())

        await asyncio.sleep(random.randrange(30, 80))

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Fresh tires', 'Models']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Let'start bussines", reply_markup=keyboard)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute())
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()