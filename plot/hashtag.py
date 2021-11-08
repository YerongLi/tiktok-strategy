import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv('../videos_dataset.csv')
cutoff_likes = np.percentile(df.likes.values.tolist(), 90)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes)]
blank_count = [eval(hashtags) for hashtags in most_liked_df.hashtag.values.tolist()]
blank_count = [1 for hashtags in blank_count if len(hashtags)==0]

freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
labels = 'HashTags', 'No HashTags'

sizes = [100-freq_blank, freq_blank]

# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# sizes = [15, 30, 45, 10]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

filename = 'hashtag.png'
plt.savefig(filename)
cwd = os.getcwd()
print(f'scp t0:{cwd}/{filename} .; open {filename}')