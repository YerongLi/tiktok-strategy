import pymongo
import tqdm
import pandas as pd
import argparse
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.tiktok

parser = argparse.ArgumentParser(description='Generate Dataset')
parser.add_argument('--file', type=str,
                    help='Input a dump of verified users e.g. verified_users.txt')
args = parser.parse_args()

videos_collection = db.videos
import multiprocessing
manager = multiprocessing.Manager()
to_save = manager.list()
def simple_dict(tiktok_dict):
  to_return = {}
  to_return['author.uniqueId'] = tiktok_dict['author']['uniqueId']
  to_return['author.id'] = tiktok_dict['author']['id']
  to_return['id'] = tiktok_dict['_id']
  to_return['desc'] = tiktok_dict['desc']
  to_return['createTime'] = tiktok_dict['createTime']
  to_return['videoduration'] = tiktok_dict['video']['duration']
  to_return['link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['author.uniqueId'], to_return['id'])
  to_return['likes'] = tiktok_dict['stats']['diggCount']
  to_return['stats.shareCount'] = tiktok_dict['stats']['shareCount']
  to_return['stats.commentCount'] = tiktok_dict['stats']['commentCount']
  to_return['stats.playCount'] = tiktok_dict['stats']['playCount']
  to_return['duetEnabled'] = tiktok_dict['duetEnabled']
  to_return['duetFromId'] = tiktok_dict['duetInfo']['duetFromId']
  to_return["stitchEnabled"] = tiktok_dict['stitchEnabled']
  to_return["shareEnabled"] = tiktok_dict['shareEnabled']
  if 'textExtra' in tiktok_dict:
      to_return['hashtag'] = [{k : tag[k] for k in ('hashtagName', 'hashtagId', 'type', 'subType')} for tag in tiktok_dict['textExtra'] if 'hashtagName' in tag and len(tag['hashtagName'])>0]
  else:
      to_return['hashtag'] = []
  if 'challenges' in tiktok_dict:
      to_return['challenges'] = [{k : challenge[k] for k in ('id', 'title', 'desc', 'isCommerce')} for challenge in tiktok_dict['challenges']]
  else:
      to_return['challenges'] = []
  if 'music' in tiktok_dict:
      to_return['music.title'] = tiktok_dict['music']['title']
  return to_return

headers = ['author.uniqueId', 'author.id', 
        'id', 'desc', 'createTime', 
        'videoduration', 'link', 
        'likes', 'stats.shareCount', 
        'stats.commentCount', 
        'stats.playCount', 
        'duetEnabled',
        'duetFromId',
        'stitchEnabled', 
        'shareEnabled',
        'hashtag',
        'challenges',
        'music.title',
        ]

content = []
with open(f'{args.file}') as f:
    lines = f.readlines()
    verified_user = set([(eval(line)['id']) for line in lines])
# print()
print(type(list(verified_user)[0]))
verified_user = ["6947197656385799174"]
for entry in tqdm.tqdm(list(videos_collection.find({'author.id': {'$in': list(verified_user)}}))):
    dic = simple_dict(dict(entry))
    content.append([dic[k] for k in headers])
df = pd.DataFrame(columns=headers, data=content)
print('finished')
df.to_csv('videos_dataset.csv', index=False)

