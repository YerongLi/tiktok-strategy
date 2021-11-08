import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv('../videos_dataset.csv')
cutoff_likes = np.percentile(df.likes.values.tolist(), 2)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes)]
print(most_liked_df.columns)
print(most_liked_df.shape[0])
blank_count = [eval(hashtags) for hashtags in most_liked_df.hashtag.values.tolist()]
for item in blank_count:
    print(item)
blank_count = [1 for hashtags in blank_count if len(hashtags)==0]

# print(most_liked_df.hashtag.values.tolist())
print(len(blank_count))
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

filename = 'hashtag.png'
plt.savefig(filename)
cwd = os.getcwd()
print(f'scp t0:{cwd}/{filename} .; open {filename}')