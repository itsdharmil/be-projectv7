import json
import pandas as pd
import numpy as np
import pulp
import sys
df=pd.read_csv('file2.csv')
def process_photo_links(text):
    start = 'https://cdn.sofifa.com/players'
    end = '19_60.png'
    id_str = str(text.split('/')[-1].split('.')[0]).zfill(6)
    return str(f'{start}/{id_str[:3]}/{id_str[3:]}/{end}')

df['photo'] = df['photo'].apply(process_photo_links)
rslt_df = df[df['id'].isin(ids)]
rslt_df.set_index("id", drop=True, inplace=True)
r=rslt_df[['name',  'nationality', 'age', 'club', 'overall', 'value','photo']]
dictionary = r.T.to_dict('list')