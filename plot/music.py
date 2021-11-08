import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import random
bins = np.linspace(0, 180, 20)
x = [None, None, None]
df = pd.read_csv('../videos_dataset.csv')
music = df['music.title'].tolist()

cutoff_likes = np.percentile(df.likes.values.tolist(), 95)
most_liked_df = df[df.likes >= int(cutoff_likes)]
blank_count = [hashtags for hashtags in most_liked_df['music.title'].values.tolist()]
blank_count = [1 for hashtags in blank_count if hashtags == 'original sound']

freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
labels = 'Famous', 'Original'

sizes = [100-freq_blank, freq_blank]

# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# sizes = [15, 30, 45, 10]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax = plt.subplots(2,2)
ax[0][0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax[0][0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[0][0].set_title('Likes: 95% top videos')


cutoff_likes = np.percentile(df.likes.values.tolist(), 75)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes)]
blank_count = [hashtags for hashtags in most_liked_df['music.title'].values.tolist()]
blank_count = [1 for hashtags in blank_count if hashtags == 'original sound']

freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
labels = 'Famous', 'Original'

sizes = [100-freq_blank, freq_blank]

# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# sizes = [15, 30, 45, 10]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

ax[0][1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax[0][1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[0][1].set_title('Likes: 75% top videos')
filename = 'music.png'
plt.savefig(filename)
cwd = os.getcwd()
print(f'scp t0:{cwd}/{filename} .; open {filename}')


