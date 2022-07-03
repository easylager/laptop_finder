import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

kufar_url = 'https://www.kufar.by/'
headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
        }




class Laptop:
    instances = {}
    def __init__(self, hash, link):
        self.__class__.instances[hash] = link
        self.hash = hash
        self.link = link


    def values(self):
        dict_item = {}
        values = list(self.__dict__.values())
        dict_item[values[0]] = values[1]
        return dict_item

    def items(self):
        return self.__dict__.items()

    @classmethod
    def hash_exist(cls, incoming_laptop_hash):
        try:
            x = bool(cls.instances[incoming_laptop_hash])
            return x
        except Exception as ex:
            return False


    def __str__(self):
        return f'{self.hash}: {self.link}'



def parsing(url):

    res = requests.get('https://www.kufar.by/l/r~minsk/noutbuki?clp=v.or%3A3%2C5%2C1%2C51%2C9&cmp=0&cnd=1&ot=0&prc=r%3A0%2C35000&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    list_of_items = soup.find('div', {"data-name": "listings"})
    items = list_of_items.find_all('section')

    for item in items:
        link = item.find('a').get('href')
        hash = link.split('/')[-1]

        if not Laptop.hash_exist(incoming_laptop_hash=link):
            result = Laptop(hash, link)




def main():
    res = requests.get(kufar_url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    list_of_items = soup.find('div', {"data-name": "listings"})
    items = list_of_items.find_all('section')

    for item in items:
        link = item.find('a').get('href')
        hash = link.split('/')[-1]




main()

