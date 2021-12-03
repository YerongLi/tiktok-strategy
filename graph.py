import pandas as pd
df = pd.read_csv('videos_dataset.csv')
authors = sorted(set(df.authors.values.tolist()))

with open('tiktok_dat/node.dat') as f:
    for author in authors:
        f.write(f'{author} a\n')
