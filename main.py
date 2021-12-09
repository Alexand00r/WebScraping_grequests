import gevent.monkey
import math

import aiohttp
import asyncio
from bs4 import BeautifulSoup
import grequests
import time
import itertools
import csv

#start_time = time.time()

links = [
    "hotel_corte_ongaro",
    "hotel_corte_santa_libera",
    "hotel_cortejo_imperial",
    "hotel_cortes",
    "hotel_cortijo",
    "hotel_cortijo_bravo",
    "hotel_cortijo_los_gallos",
    "hotel_cortijo_torre_de_la_reina",
    "hotel_corvatsch",
    "hotel_corvetto"
]


def exception_handler(request, exception):
    print(f"Request failed. Url: {request.url}.\nException: {exception}")


def write_down_results(results):
    separator = "\n"
    results_string = separator.join(results) + "\n"
    with open("code_with_rating_async.txt", "a", encoding='utf-8') as file:
        file.write(results_string)
    results.clear()


hotel_code_file = open("map_list.txt", encoding="utf-8-sig")
hotel_code_rows = hotel_code_file.read().splitlines()

proxy_file = open("proxy_list.txt", encoding="utf-8-sig")
proxy_lines = proxy_file.read().splitlines()
if len(hotel_code_rows) > len(proxy_lines):
    multiply = math.ceil(len(hotel_code_rows)/len(proxy_lines))
    proxy_lines *= multiply

proxies = []
for host in proxy_lines:
    proxies.append(dict(http='http://' + host, https='https://' + host))


async def run():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get("https://yandex.ru/") as resp:
            print(BeautifulSoup(await resp.content, 'html.parser'))

loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)


#print("--- %s seconds ---" % (time.time() - start_time))
