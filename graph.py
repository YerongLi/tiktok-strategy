import pandas as pd
df = pd.read_csv('videos_dataset.csv')
authors = sorted(set(df['author.uniqueId'].values.tolist()))
videos = sorted(set(df.id.values.tolist()))

with open('tiktok_data/node.dat', 'w') as f:
    for author in authors:
        f.write(f'{author} a\n')
    for video in videos:
        f.write(f'{video} v\n')

with open('tiktok_data/link.dat', 'w') as f:
    for i in range(df.shape[0]):
        f.write(f"{df.iloc[i]['author.uniqueId']} {df.iloc[i].id}\n")
