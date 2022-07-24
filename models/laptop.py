import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver


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



