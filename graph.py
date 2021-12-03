import pandas as pd
import logging

df = pd.read_csv('videos_dataset.csv')
a = set(df.id.values.tolist())
b = set(df.duetFromId.values.tolist())

logging.basicConfig(level=logging.DEBUG)
logging.debug(f'There are {len(a)} vidoes and {len(b)} dueted videos : {len(len(a.union(b)))} videos in total.')

for i in b:
    if i != 0:
        print(i)
        break
with open('tiktok_data/node.dat', 'w') as f:
    for author in sorted(set(df['author.uniqueId'].values.tolist())):
        f.write(f'{author} a\n')
    for video in sorted(set(df.id.values.tolist()).union(set(df.duetFromId.values.tolist()))):
        f.write(f'{video} v\n')
    for music in sorted(set(df['music.title'].values.astype(str).tolist()), key=len):
        f.write(f'{music} m\n')

with open('tiktok_data/link.dat', 'w') as f:
    for i in range(df.shape[0]):
        f.write(f"{df.iloc[i]['author.uniqueId']} {df.iloc[i].id}\n")
        f.write(f"{df.iloc[i].id} {df.iloc[i]['author.uniqueId']}\n")
        f.write(f"{df.iloc[i].id} {df.iloc[i]['music.title']}\n")
        F.write(f"{df.iloc[i].id}")
