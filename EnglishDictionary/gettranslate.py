import requests
from lxml import etree
from bs4 import BeautifulSoup
import csv


def translate(keyword):
    url= f'https://cn.bing.com/dict/search?q={keyword}&qs=n&form=Z9LH5&sp=-1&lq=0&pq=perform&sc=8-7&sk=&cvid=9E6CCD85275A40BF92D28C596BB4B399'
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text,'lxml')
    result = soup.find('div',class_='qdef').find('ul').text

    source0 = soup.find('div',class_='hd_tf').find('a').attrs
    source = 'https://cn.bing.com/'+ source0['data-mp3link']
    down_audio(source,keyword)
    return result
    #print(result)
    #print(source)

def down_audio(url,filename):
    response = requests.get(url)
    with open(f'D:\\Py100\\Python_100_Days\\EnglishDictionary\\audios\\{filename}.mp3','wb') as f:
        f.write(response.content)

def read_text():

    csv_file = open('words.csv','w',encoding='utf-8',newline='')
    csv_row = csv.writer(csv_file)
    csv_row.writerow(['Englishword','means','path'])
    file = open(r'D:\Py100\Python_100_Days\EnglishDictionary\wordlist1\word.txt','r',encoding='utf-8')
    lines = file.readlines()
    #print(lines)
    for i in lines:
        item = i.replace('\n','')
        # print(item)
        means = translate(item)
        row = [item,means,f'D:\\Py100\\Python_100_Days\\EnglishDictionary\\audios\\{item}.mp3']
        print(item,means)
        csv_row.writerow(row)

# translate('new')
read_text()







