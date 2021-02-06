""" # text = "https://cdn.sofifa.org/players/4/19/167495.png"
# def process_photo_links(text):
#     start = 'https://cdn.sofifa.com/players'
#     end = '19_60.png'
#     id_str = str(text.split('/')[-1].split('.')[0]).zfill(6)
#     return str(f'{start}/{id_str[:3]}/{id_str[3:]}/{end}')
# # df['photo'] = df['photo_id'].apply(lambda x: f'/assets/players/{x}.png')

# print(process_photo_links("https://cdn.sofifa.org/players/4/19/158023.png"))
# https://cdn.sofifa.com/players/158/023/19_60.png


import requests
from bs4 import BeautifulSoup
import os
link="https://cdn.sofifa.com/players/158/023/19_60.png"


# def scrape_player_photos(path):

#     response = requests.get(link)
#     with open(f"{path}/{'158023'}.jpg", 'wb') as f:
#         f.write(response.content)

# PATH = '../'
# scrape_player_photos(PATH)
url=link
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('img')
print(images)
 """




## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

## Set up the image URL and filename
image_url = "https://cdn.sofifa.com/players/158/023/19_180.png"
filename = image_url.split("/")[-3]+image_url.split("/")[-2]+".jpg"

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    from os import path

    file_path = path.relpath(filename)
    with open(file_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    # with open(fimage'+filename,'wb') as f:
        # shutil.copyfileobj(r.raw, f)
        
    print('Image sucessfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retreived')