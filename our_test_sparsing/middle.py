import csv
import requests
from bs4 import BeautifulSoup

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


def all_cars(normhtml): 
    list=[]
    a=normhtml.find('div',class_='category-block cars')
    all_cars=a.find_all("div",class_='modal-main-title')
    h=normhtml.find('div',class_='category-block')
    each_cars=h.find_all('div',class_='category-block-content-item')
    c=normhtml.find_all('div',class_='tmb-wrap')
    dfg={}
    for x in all_cars:
        x=x.text.strip()
        dfg.update({'nameofmodel':x})
        # print(x)
    #     #x = это все названия моделеей
    for one_car in each_cars:
        a=one_car.find('a').get('href')
        a=f'https://www.mashina.kg{a}'
        list.append(a)
    for dvd in list:
        bad_html=get_html(dvd)
        good_html=get_soup(bad_html)
        df=good_html.find('div',class_='price-dollar')
        # print(df.text.strip())
        description=good_html.find('h2',class_='comment')
        # print(x+'-'+df.text.strip()+'\n',description.text.strip())
        for dsg in dfg.values():
            print(dsg)
            print()
            print(df.text.strip())
            print()
            print(description.text.strip())
        # df - это все цены

url='https://www.mashina.kg/'
html=get_html(url)
normhtml=get_soup(html)
models=all_cars(normhtml)
print(models)
