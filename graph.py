import pandas as pd
import logging
import tqdm

df = pd.read_csv('videos_dataset.csv')
a = set(df.id.values.tolist())
b = set(df.duetFromId.values.tolist())
b.remove(0)

logging.basicConfig(level=logging.DEBUG)
logging.info(f'There are {len(a)} vidoes and {len(b)} dueted videos : {len(a.union(b))} videos in total.')

with open('tiktok_data/node.dat', 'w') as f:
    for author in sorted(set(df['author.uniqueId'].values.tolist())):
        f.write(f'{author} a\n')
    for video in sorted(a.union(b)):
        f.write(f'{video} v\n')
    for music in sorted(set(df['music.title'].values.astype(str).tolist()), key=len):
        if music != 'original sound'
        f.write(f'{music} m\n')

with open('tiktok_data/link.dat', 'w') as f:
    for i in tqdm.tqdm(range(df.shape[0])):
        f.write(f"{df.iloc[i]['author.uniqueId']} {df.iloc[i].id}\n")
        f.write(f"{df.iloc[i].id} {df.iloc[i]['author.uniqueId']}\n")
        if df.iloc[i]['music.title'] != 'original sound':
            f.write(f"{df.iloc[i]['music.title']} {df.iloc[i].id}\n")
        if df.iloc[i].duetFromId != 0:
            f.write(f"{df.iloc[i].duetFromId} {df.iloc[i].id}\n")
