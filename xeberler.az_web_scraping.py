from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
News = []
for i in range(1,41):
    url = f"https://xeberler.az/new/content/all/{i}"
    get_content = requests.get(url).content
    page = BeautifulSoup(get_content,'lxml')
    news_list = page.find_all('div',class_='sec-topic')

    for news in news_list:
        scrap_time = datetime.now()
        header = news.find('h3').text
        link = news.a['href']
        date = news.find('div',class_='time').text.strip()
        photo_url = news.find('img',class_="img-thumbnail cat-big-img")['src']
        get_content2 = requests.get(link).content
        news_page = BeautifulSoup(get_content2,'lxml')
        text = news_page.find('div',class_='time').text
        index = text.index('/') + 1
        news_time = text[index:]
        topic = news_page.find('h1').text
        info = news_page.find('div',class_="news-details-all").text.replace('\n','')
        News.append([header,link,photo_url,date,news_time,topic,info,scrap_time])

df = pd.DataFrame(News,columns=['Başlıq','Link','Foto url','Tarix','Saat','Kateqoriya','Xəbər','Scrap tarixi'])
df.to_csv("Xəbərlər_az.csv",index=False)