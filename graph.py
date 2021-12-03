import pandas as pd
df = pd.read_csv('videos_dataset.csv')
authors = sorted(set(df.author.values.tolist()))
videos = sorted(set(df.author.values.tolist()))

with open('tiktok_dat/node.dat', 'w') as f:
    for author in authors:
        f.write(f'{author} a\n')
    for video in videos:
        f.write(f'{video} v\n')
