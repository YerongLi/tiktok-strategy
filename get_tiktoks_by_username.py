from TikTokApi import TikTokApi
import pandas as pd
import tqdm
import pickle
api = TikTokApi.get_instance()

db = client.tiktok

count = 3
usernames = list(set(pd.read_csv('final_data.csv')['author.unique_id'].values.tolist()))[:2000]
print(len(set(usernames)))
# print(len(authors))
# print(pd.read_csv('final_data.csv').columns)
# usernames = ['andyr00']

usernames_ = []
for username in tqdm.tqdm(usernames):
    try:
        api.get_user(username)
        usernames_.append(username)     
    except:
        pass
del usernames
print(len(usernames_))
with open('usernames.pkl', 'wb') as f:
    pickle.dump(usernames_, f)
    # tiktoks = api.by_username(username, count=count)

    # for tiktok in tiktoks:
    #     print(tiktok)
