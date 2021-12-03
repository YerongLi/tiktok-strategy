import pandas as pd
df = pd.read_csv('videos_dataset.csv')

with open('tiktok_data/node.dat', 'w') as f:
    for author in sorted(set(df['author.uniqueId'].values.tolist())):
        f.write(f'{author} a\n')
    for video in sorted(set(df.id.values.tolist())):
        f.write(f'{video} v\n')
    for music in sorted(set(df['music.title'].values.tolist())):
        f.write(f'{music} m\n')

with open('tiktok_data/link.dat', 'w') as f:
    for i in range(df.shape[0]):
        f.write(f"{df.iloc[i]['author.uniqueId']} {df.iloc[i].id}\n")
        f.write(f"{df.iloc[i].id} {df.iloc[i]['author.uniqueId']}\n")
        f.write(f"{df.iloc[i].id} {df.iloc[i]['music.title']}\n")


# with open()
