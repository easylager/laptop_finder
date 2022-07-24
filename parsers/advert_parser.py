import requests
import re

from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

from handlers.config_handlers import UserAgentsHandler, ProxiesHandler
from config.enums.enums import ParseTemplate
from models.url import AbstractUrl


class AdvertParser:

    def __init__(self, url):
        self.url = AbstractUrl(full_url=url)

    @property
    def response(self):
        return requests.get(
            url=self.url,
            headers=UserAgentsHandler.header(),
            proxies=ProxiesHandler.proxy()
        ).text

    @property
    def advert_object(self):
        return BeautifulSoup(self.response, 'lxml')

    @property
    def price(self):
        return self.advert_object.find('div', class_=re.compile(ParseTemplate.FOR_PRICE.value)).text

    @property
    def title(self):
        return self.advert_object.find('h1', class_=re.compile(ParseTemplate.FOR_TITLE.value)).text

    @property
    def time(self):
        return self.advert_object.find('span', class_=ParseTemplate.FOR_TIME.value).text

    @property
    def address(self):
        return self.advert_object.find('span', class_=ParseTemplate.FOR_ADDRESS.value).text

    @property
    def parameters(self):
        """returns tuple of advert parameters"""

        parameters = self.advert_object.find_all(
            'div', class_=ParseTemplate.FOR_PARAMETERS.value
        )

        return tuple(parameter.text for parameter in parameters)




