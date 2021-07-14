# from amazon_product_review_scraper import amazon_product_review_scraper
# review_scraper = amazon_product_review_scraper(amazon_site="amazon.in", product_asin="B07X6V2FR3")
# reviews_df = review_scraper.scrape()
# print(reviews_df.head(5))


import requests
from bs4 import BeautifulSoup
import pandas as pd

reviewlist = []

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass

for x in range(1,999):
    
    soup = get_soup(f'https://www.amazon.in/iQOO-Legend-Legendary-Design-Storage/dp/B08697MJFD/ref=br_msw_pdt-5?_encoding=UTF8&smid=AQUYM0O99MFUT&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=4W75HWFN2SKS6Y318RQ7&pf_rd_t=36701&pf_rd_p=5b42e6ae-1ba8-4d9f-b00b-b2fe636d1de6&pf_rd_i=desktop&th=1')
    soup = get_soup(f'https://www.amazon.co.uk/product-reviews/B07WD58H6R/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_excel('sony-headphones.xlsx', index=False)
print('Fin.')