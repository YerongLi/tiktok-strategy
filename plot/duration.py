import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import random
x = [None, None, None]
df = pd.read_csv('../videos_dataset.csv')
cutoff_likes95 = np.percentile(df.likes.tolist(), 95)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes95)]

x[0] = most_liked_df.videoduration.values.tolist()
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# pyplot.hist(x, bins, alpha=0.5, label='x')
# pyplot.hist(y, bins, alpha=0.5, label='y')
bins = np.linspace(0, 10000, 10000)
cutoff_likes75 = np.percentile(df.likes.values.tolist(), 75)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes75)]
most_liked_df = most_liked_df[most_liked_df.likes < int(cutoff_likes95)]
# x[0] = [random.gauss(3,1) for _ in range(400)]
# x[1] = [random.gauss(4,2) for _ in range(400)]
x[1] = most_liked_df.videoduration.values.tolist()


fig1, ax = plt.subplots(2,1)
ax[0].hist(x[0], alpha=0.3, label='95%')
ax[0].hist(x[1], alpha=0.3, label='75%')
ax[0].set_title('Likes : top videos')




cutoff_likes95 = np.percentile(df['stats.playCount'].values.tolist(), 95)
# print(cutoff_likes)
most_liked_df = df[df['stats.playCount'] >= int(cutoff_likes95)]

x[0] = most_liked_df.videoduration.values.tolist()
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# pyplot.hist(x, bins, alpha=0.5, label='x')
# pyplot.hist(y, bins, alpha=0.5, label='y')
bins = np.linspace(0, 10000, 10000)
cutoff_likes75 = np.percentile(df['stats.playCount'].values.tolist(), 75)
# print(cutoff_likes)
most_liked_df = df[df['stats.playCount'] >= int(cutoff_likes75)]
most_liked_df = most_liked_df[most_liked_df['stats.playCount'] < int(cutoff_likes95)]
# x[0] = [random.gauss(3,1) for _ in range(400)]
# x[1] = [random.gauss(4,2) for _ in range(400)]
x[1] = most_liked_df.videoduration.values.tolist()


fig1, ax = plt.subplots(2,1)
ax[1].hist(x[0], alpha=0.3, label='95%')
ax[1].hist(x[1], alpha=0.3, label='75%')
ax[1].set_title('Likes : top videos')

# cutoff_likes = np.percentile(df.likes.values.tolist(), 75)
# # print(cutoff_likes)
# most_liked_df = df[df.likes >= int(cutoff_likes)]
# blank_count = [eval(hashtags) for hashtags in most_liked_df.hashtag.values.tolist()]
# blank_count = [1 for hashtags in blank_count if len(hashtags)==0]

# freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
# labels = 'HashTags', 'No HashTags'

# sizes = [100-freq_blank, freq_blank]

# # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# # sizes = [15, 30, 45, 10]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# ax[0][1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax[0][1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax[0][1].set_title('Likes: 75% top videos')



# cutoff_likes = np.percentile(df['stats.playCount'].values.tolist(), 95)
# # print(cutoff_likes)
# most_liked_df = df[df['stats.playCount'] >= int(cutoff_likes)]
# blank_count = [eval(hashtags) for hashtags in most_liked_df.hashtag.values.tolist()]
# blank_count = [1 for hashtags in blank_count if len(hashtags)==0]

# freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
# labels = 'HashTags', 'No HashTags'

# sizes = [100-freq_blank, freq_blank]

# # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# # sizes = [15, 30, 45, 10]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# ax[1][0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax[1][0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax[1][0].set_title('Views: 95% top videos')


# cutoff_likes = np.percentile(df['stats.playCount'].values.tolist(), 75)
# # print(cutoff_likes)
# most_liked_df = df[df['stats.playCount'] >= int(cutoff_likes)]
# blank_count = [eval(hashtags) for hashtags in most_liked_df.hashtag.values.tolist()]
# blank_count = [1 for hashtags in blank_count if len(hashtags)==0]

# freq_blank = len(blank_count)/ most_liked_df.shape[0] * 100
# labels = 'HashTags', 'No HashTags'

# sizes = [100-freq_blank, freq_blank]

# # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

# # sizes = [15, 30, 45, 10]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# ax[1][1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax[1][1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax[1][1].set_title('Views: 75% top videos')
filename = 'duration.png'
plt.savefig(filename)
cwd = os.getcwd()
print(f'scp t0:{cwd}/{filename} .; open {filename}')