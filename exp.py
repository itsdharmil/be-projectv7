# text = "https://cdn.sofifa.org/players/4/19/167495.png"
def process_photo_links(text):
    start = 'https://cdn.sofifa.com/players'
    end = '19_60.png'
    id_str = str(text.split('/')[-1].split('.')[0]).zfill(6)
    return str(f'{start}/{id_str[:3]}/{id_str[3:]}/{end}')
# df['photo'] = df['photo_id'].apply(lambda x: f'/assets/players/{x}.png')

print(process_photo_links("https://cdn.sofifa.org/players/4/19/158023.png"))

import requests
from bs4 import BeautifulSoup
import os
link="https://cdn.sofifa.org/players/4/19/158023.png"
im = requests.get(link)
    