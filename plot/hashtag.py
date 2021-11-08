import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../videos_dataset.csv')
cutoff_likes = np.percentile(df.likes.values.tolist(), 90)
# print(cutoff_likes)
most_liked_df = df[df.likes >= int(cutoff_likes)]
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()