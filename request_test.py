import requests
from bs4 import BeautifulSoup
import urllib3

'3'
htttp_manager = urllib3.PoolManager()
response_req = requests.get('https://www.kufar.by/l/r~minsk/noutbuki?clp=v.or%3A3%2C5%2C1&ot=0&prc=r%3A0%2C30000&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d')
response = htttp_manager.request('GET', 'https://www.kufar.by/l/r~minsk/noutbuki?clp=v.or%3A3%2C5%2C1&ot=0&prc=r%3A0%2C30000&query=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA&sort=lst.d')
print(type(response))
bs_object = BeautifulSoup(response.data, 'lxml')
list_of_items = bs_object.find('div', {"data-name": "listings"})
bs_obj_req = BeautifulSoup(response_req.text, 'lxml')
list_of_items_req = bs_obj_req.find('div', {"data-name": "listings"})
print(list_of_items)
print(list_of_items_req)