from bs4 import BeautifulSoup
import requests
import csv
def get_html(url):
    """Получает html  разметку определленого сайта по url"""
    response=requests.get(url)
    return response.text


def get_last_page(soup) ->int:
    """возвращает последнюю страницу на сайте"""
    pages=soup.find('ul',class_='pagination').find_all('a',class_='page-link')
    last_page=pages[-1].get('data-page')
    return int(la)


def get_soup(html):
    """НАша функция получает html разметку и структурирует её в  bs"""
    soup=BeautifulSoup(html,'html.parser')
    return soup

def det_data(soup:BeautifulSoup):
    """функция парсер,получает нужные данные с сайта и возвращает в виде списка"""
    container=soup.find('div',class_='table-view-list')
    cars=container.find_all('div',class_='list-item')
    result=[]
    for car in cars:
        name= car.find('h2',class_='name').contents[0].strip()
        try:
            img=car.find('img',class_='lazy-image').get('data-src')
        except:
            img='No image!'
        price_div=car.find('div',class_='price')
        price=price_div.find('p').text
        price_dollar=price_div.find('p').find('strong').text
        # desc1=car.find('p',class_='year-miles').text.strip()
        # desc2=car.find('p',class_='body-type').text.strip()
        # desc3=car.find('p',class_='volume').text.strip()
        # description=f'{desc1}{desc2}{desc3}'
        # print(description)
        ls=['year-miles','body-type','volume']
        desc=''.join(car.find('p',class_=x).text.strip() for x in ls)
        data={
            'name':name,'desc':desc,'price':price,'img':img        }
        result.append(data)
    return result
        # print(desc)
        # break

def prepare_csv():
    '''функция подготавливает scv файл'''
    with open('cars.csv','w') as file:
        fieldnames=['№','Name','descriprion','price','Image url']
        writer=csv.DictWriter(file,fieldnames)
        writer.writerow({
            '№':count,
            'name':car['name'],
            'description':car['desc'],
            'price':car['price'],
            'Image Url':car['img']
            })
def write_to_csv(data):
    '''Записывает все данные csv файл'''
    with open('cars.csv','a') as file:
        fieldnames=['№','Name','descriprion','price','Image url']
        writer=csv.DictWriter(file,fieldnames)
        global count
        for car in data:
            writer.writerow({
            '№':count,
            'name':car['name'],
            'description':car['desc'],
            'price':car['price'],
            'image':car['img']
            })
def main():
    i=1
    while True:
        url=f'https://www.mashina.kg/search/all/?page={i}'
        html=get_html(url)
        soup=get_soup(html)
        print(det_data(soup))
        print(f'спарсили{i}/{get_last_page} страницу!')
        if i==15:
            break
        i +=1

# main()