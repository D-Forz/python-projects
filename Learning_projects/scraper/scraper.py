import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapping_xakata():
    results = []
    url= 'https://www.xataka.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    article_list = soup.find('div', {'class' : 'section-recent-list'})
    article = article_list.find('article', {'class' : 'recent-abstract abstract-article'})
    link = article.a['href']
    title = article.h2.text
    for url in range(1):
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        article_content = soup.find('div', {'class' : 'article-content'})
        article = article_content.find('div', {'class' : 'blob js-post-images-container'})
        description = article.get_text().replace("\xa0", "").strip().split("\n")[:-1]
        description_clean = " ".join(description)
    results.extend([title, link, description_clean])
    return results

scrapping_xakata()