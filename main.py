import math

from bs4 import BeautifulSoup
import grequests
import time
from fp.fp import FreeProxy
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

reqs = []
for hotel_code_row, proxy in zip(hotel_code_rows, proxies):
    hotel_code_bytes = hotel_code_row.encode()
    hotel_code = hotel_code_bytes.decode()
    url = "https://ostrovok.ru/rooms/" + hotel_code
    #reqs.append(grequests.get(url, proxies=proxy))
    reqs.append(grequests.get(url))

resps = grequests.imap(reqs, grequests.Pool(10), exception_handler=exception_handler)

results = []
count = 0
for resp in resps:
    if count == 3:
        write_down_results(results)
        count = 0

    soup = BeautifulSoup(resp.text, 'lxml')
    rating_img_tag = soup.find_all('img', attrs={"class": 'zen-tripadvisor-rating-main'})
    hotel_url_tag = soup.find_all('link', attrs={"rel": 'canonical'})
    hotel_url_text = hotel_url_tag[0]['href'].split("/")
    hotel_code_text = hotel_url_text[-1] if hotel_url_text[-1] else hotel_url_text[-2]

    try:
        result_element = "\"" + hotel_code_text + "\"; " + rating_img_tag[0]['alt']
        print(result_element)
        results.append(result_element)
    except:
        result_element = "\"" + hotel_code_text + "\"; null"
        print(result_element)
        results.append(result_element)

    count += 1

if count > 0:
    write_down_results(results)
    count = 0

#print("--- %s seconds ---" % (time.time() - start_time))
