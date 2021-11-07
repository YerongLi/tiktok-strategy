from TikTokApi import TikTokApi
import pandas as pd
import tqdm
api = TikTokApi.get_instance()

count = 3
usernames = set(pd.read_csv('final_data.csv')['author.unique_id'].values.tolist())
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
    # tiktoks = api.by_username(username, count=count)

    # for tiktok in tiktoks:
    #     print(tiktok)
