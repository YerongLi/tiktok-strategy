import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import random
bins = np.linspace(0, 180, 20)
x = [None, None, None]
df = pd.read_csv('../videos_dataset.csv')
music = df['music.title'].tolist()
print(music)