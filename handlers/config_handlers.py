from abc import ABC, abstractmethod
import random


class ConfigHandler(ABC):

    PATH = 'config/proxies'

    @classmethod
    @abstractmethod
    def handle(cls, path=PATH):
        with open(path) as file:
            configs = file.read().split('\n')
        return configs

    @classmethod
    @abstractmethod
    def get_random(cls):
        return random.choice(cls.handle())

class ProxiesHandler(ConfigHandler):

    @classmethod
    def proxy(cls):
        return {'http': f'http//{cls.get_random()}'}

class UserAgentsHandler(ConfigHandler):

    PATH = 'config/useragents'

    @classmethod
    def header(cls):
        return {'user-agent': cls.get_random()}
