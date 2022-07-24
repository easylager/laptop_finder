from parsers.advert_parser import AdvertParser
from aiogram.utils.markdown import hbold, hlink

class ResponseConstructor:

    def __init__(self, parser: AdvertParser):
        self.parser = parser

    def build_response(self):
        #return f"{hlink(self.parser.title, self.parser.url)}"
        return f'{hlink(self.parser.title, self.parser.url)}\n' \
               f'{hbold(self.parser.price)}\n' \
               f'--------------------\n' \
               f'{hbold(self.parser.parameters)}'


