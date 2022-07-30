from enum import Enum


class BaseEnum(Enum):

    def __str__(self):
        return self.value

class Goods(BaseEnum):
    LAPTOPS = 'https://www.kufar.by/l/r~minsk/noutbuki?clp=v.or%3A3%2C5%2C1&ot=0&prc=r%3A0%2C30000&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d'
    DDR = '' #need to add
    LAPTOPS_TEST = 'https://www.kufar.by/l/r~minsk/noutbuki?ot=0&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%B8&utm_search=Category%20only'


class ParseTemplate(BaseEnum):
    FOR_PRICE = '.*__price__.*'
    FOR_TITLE = '.*__title__.*'
    FOR_TIME = '.*__time__.*'
    FOR_ADDRESS = '.*_address__.*'
    FOR_PARAMETERS = '.*_parameter_value__.*'

