import requests
from bs4 import BeautifulSoup as bs
import json




def get_html(url):
    """получаем html код с страницы,но он непонятный и внем нельзя сориентироваться"""
    #получаем непонятную кашу из html
    response=requests.get(url)
    return response.text


def get_soup(html):
    """делаем код более понятным"""
    #делаем html код более понятным
    soup=bs(html,'lxml')
    return soup


def get_catalog(soup):
    """получаем каталог с новостями"""
    catalog=soup.find('div',class_='Tag--articles')
    return catalog


def get_atricles(catalog):
    """получаем все новости в каталоге"""
    articles=catalog.find_all('div',class_='Tag--article')[0:20]
    return articles


def get_detail(link):
    """получаем здесь картинку и описание с каждого подзаголовка"""
    from functools import reduce
    html=get_html(link)
    soup=get_soup(html)
    #получаем тот самый контейнер
    container=soup.find('div',class_='BbCode')
    #zвытаскиваем все строки описания           
    text=container.find_all('p')
    res=reduce(lambda a,b:a+ '\n'+ b,[x.text.strip() for x in text])
    return res
get_detail('https://kaktus.media/doc/479629_kinyl_moshennikov._v_moskve_taksist_jenishbek_vernyl_polmilliona_84_letney_jenshine.html')

def get_data(articles):
    '''вытаскиваем наши заголовки,картинки, описания.Записываем все в dictionary'''
    i=1
    res={}
    #проходимся по html коду каждой новости и вытвскиваем title,image,
    for item in articles:
        title=item.find('a', class_='ArticleItem--name').text.strip()
        #вытаскиваем ссылку картинки и для того чтобы картинка была большая,в url меняем 'small' на 'big'
        image=item.find('img', class_='ArticleItem--image-img').get('src')
        image=image.replace('small','big')
        #берем ссылку каждой страницы каждой новости
        link=item.find('a', class_='ArticleItem--name').get('href')
        description=get_detail(link)
        #записываем это все в dict
        data={'title':title,'img':image,'desc':description}
        res[i]=data
        i +=1
    return res


def write_to_json(data):
    '''записываем все наши данные в json file'''
    with open('data.json','w') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)




def parse_news():
    '''запускаем все наши функции'''
    base_url='https://kaktus.media/?lable=8&date=2023-04-25&order=time'
    html=get_html(base_url)
    soup=get_soup(html)
    catalog=get_catalog(soup)
    articles=get_atricles(catalog)
    data=get_data(articles)
    write_to_json(data)

# parse_news()