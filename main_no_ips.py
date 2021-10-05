from bs4 import BeautifulSoup
import grequests
import time

start_time = time.time()

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

reqs = (grequests.get("https://ostrovok.ru/rooms/" + link) for link in links)
resp = grequests.imap(reqs, grequests.Pool(10))

for r in resp:
    soup = BeautifulSoup(r.text, 'lxml')
    rating_img_tag = soup.find_all('img', attrs={"class": 'zen-tripadvisor-rating-main'})
    hotel_url_tag = soup.find_all('link', attrs={"rel": 'canonical'})
    hotel_url_text = hotel_url_tag[0]['href'].split("/")
    hotel_code_text = hotel_url_text[-1] if hotel_url_text[-1] else hotel_url_text[-2]

    try:
        print("\"" + hotel_code_text + "\"; " + rating_img_tag[0]['alt'])
    except:
        print("\"" + hotel_code_text + "\"; null")

print("--- %s seconds ---" % (time.time() - start_time))
