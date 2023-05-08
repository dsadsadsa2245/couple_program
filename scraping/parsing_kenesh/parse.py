import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Pool



def get_html(url):
    """получаем html код с страницы,но он непонятный и внем нельзя сориентироваться"""
    #получаем непонятную кашу из html
    response=requests.get(url)
    return response.text


def get_soup(html):
    """делаем код более понятным"""
    #делаем html код более понятным
    soup=BeautifulSoup(html,'html.parser')
    return soup


def get_1page_links(soup):
    """ берем страницу каждого депутата и запихиваем в список links.Принимает он готовый красивый код html"""
    links=[]
    #находим всех депутатов
    container=soup.find('div',class_='grid-deputs')
    #внутри всех депутатов находим отдельные карточки депутатов.Используем find_all так как карточки одинаковы
    items=container.find_all('div',class_='dep-item')
    for item in items:
        #находим все ссылки.get используем потому что это атрибут.А когда тег,мы используем find
        a=item.find('a').get('href')
        #ссылки на сайте не содержат http://kenesh.kg. Поэтому мы конкотенируем.
        link='http://kenesh.kg'+a
        links.append(link)
        print(links)
    return links

def get_all_links():
    """собрали ссылки страниц каждого депутата и запихнули в список, также выводим кол-во депутатов"""
    res=[]
    for i in range(1,6):
        url=f'http://kenesh.kg/ru/deputy/list/35?page={i}'
        html=get_html(url)
        soup=get_soup(html)
        page_links=get_1page_links(soup)
        res.extend(page_links)
    return res


def get_deps_data(link):
    """принимаем ссылку отдельной страницы какого-либо депутата.И отображаем его данные"""
    html=get_html(link)
    soup=get_soup(html)
    #принимаем имя,информацию,биографию
    name=soup.find('div', class_="deput-name").text
    info="".join(soup.find('div',class_='deput-info').text.strip().split())
    bio=soup.find('div',class_='tab-content').text.strip()
    # img будет в виде ссылки
    img='http://kenesh.kg'+soup.find('div',class_='deput-image').find('img').get('src')
    data={'name':name,'info':info,'bio':bio,'img':img,'link':link}
    return data



def prepare_csv():
    with open('deputy.csv','w') as file:
        writer=csv.writer(file)
        writer.writerow(['FIO','Info','Bio','Image','Link to page'])


def write_to_csv(data):
    with open('deputy.csv','a') as file:
        writer=csv.writer(file)
        writer.writerow([data['name'],data['info'],data['bio'],data['img'],data['link']])
        print(f'{data["name"]}- parsed')



def make_all(link):
    data=get_deps_data(link)
    write_to_csv(data)
    




def main():
    prepare_csv()
    links=get_all_links()
    # for link in links:
    #     data=get_deps_data(link)
    #     write_to_csv(data)
    """параллельно(много одновремено)"""
    with Pool(60) as pool:
        pool.map(make_all,links)

if __name__=='__main__':
    start=datetime.now()
    main()
    finish=datetime.now()
    print(f'Parsing takes {finish - start} time! ')

# 76 секунд!!!!