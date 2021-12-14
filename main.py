import asyncio
import aiohttp

hotel_code_file = open("map_list.txt", encoding="utf-8-sig")
hotel_code_rows = hotel_code_file.read().splitlines()


async def go_ostrovok(hotel_code):

    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org", proxy="https://3.84.87.10:3128", ssl=False) as response:

            html = await response.text()
            toFileText = f"\n{response.status} {hotel_code}"

            with open("code_with_rating_async.txt", "a", encoding='utf-8') as file:
                file.write(toFileText)


async def main():
    await asyncio.gather(*[go_ostrovok(hotel_code) for hotel_code in hotel_code_rows])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())





#import gevent.monkey
#import math

#import aiohttp
#import asyncio
#from bs4 import BeautifulSoup
#import grequests
#import time
#import itertools
#import csv

#start_time = time.time()

#links = [
#    "hotel_corte_ongaro",
#    "hotel_corte_santa_libera",
#    "hotel_cortejo_imperial",
#    "hotel_cortes",
#    "hotel_cortijo",
#    "hotel_cortijo_bravo",
#    "hotel_cortijo_los_gallos",
#    "hotel_cortijo_torre_de_la_reina",
#    "hotel_corvatsch",
#    "hotel_corvetto"
#]

#headers = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#    "Accept-Encoding": "gzip, deflate, br",
#    "Accept-Language": "ru,en;q=0.9",
#    "Host": "ya.ru",
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.2.773 Yowser/2.5 Safari/537.36"
#}


#def exception_handler(request, exception):
#    print(f"Request failed. Url: {request.url}.\nException: {exception}")


#def write_down_results(results):
#    separator = "\n"
#    results_string = separator.join(results) + "\n"
#    with open("code_with_rating_async.txt", "a", encoding='utf-8') as file:
#        file.write(results_string)
#    results.clear()


#hotel_code_file = open("map_list.txt", encoding="utf-8-sig")
#hotel_code_rows = hotel_code_file.read().splitlines()

#proxy_file = open("proxy_list.txt", encoding="utf-8-sig")
#proxy_lines = proxy_file.read().splitlines()
#if len(hotel_code_rows) > len(proxy_lines):
#    multiply = math.ceil(len(hotel_code_rows)/len(proxy_lines))
#    proxy_lines *= multiply

#proxies = []
#for host in proxy_lines:
#    proxies.append(dict(http='http://' + host, https='https://' + host))


#async def run():
#    async with aiohttp.ClientSession(trust_env=True) as session:
#        async with session.get("https://ya.ru/", headers = headers) as resp:
#            with open("code_with_rating_async.txt", "a", encoding='utf-8') as file:
#                file.write("\n" + str(resp.status))

#loop = asyncio.get_event_loop()

#future = asyncio.ensure_future(run())
#loop.run_until_complete(future)


#print("--- %s seconds ---" % (time.time() - start_time))
