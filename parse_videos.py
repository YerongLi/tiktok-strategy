import pymongo
import tqdm
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.tiktok

videos_collection = db.videos
import multiprocessing
manager = multiprocessing.Manager()
to_save = manager.list()
def simple_dict(tiktok_dict):
  to_return = {}
  to_return['author.uniqueId'] = tiktok_dict['author']['uniqueId']
  to_return['author.id'] = tiktok_dict['author']['id']
  to_return['id'] = tiktok_dict['id']
  to_return['desc'] = tiktok_dict['desc']
  to_return['createTime'] = tiktok_dict['createTime']
  to_return['videoduration'] = tiktok_dict['video']['duration']
  to_return['link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['author.uniqueId'], to_return['id'])
  to_return['likes'] = tiktok_dict['stats']['diggCount']
  to_return['stats.shareCount'] = tiktok_dict['stats']['shareCount']
  to_return['stats.commentCount'] = tiktok_dict['stats']['commentCount']
  to_return['stats.playCount'] = tiktok_dict['stats']['playCount']
  to_return["duetEnabled"] = tiktok_dict['duetEnabled']
  to_return["stitchEnabled"] = tiktok_dict['stitchEnabled']
  to_return["shareEnabled"] = tiktok_dict['shareEnabled']
  if 'textExtra' in tiktok_dict:
      to_return['hashtag'] = [{k : tag[k]} for k in ('hashtagName', 'hashtagId', 'type', 'subType')for tag in tiktok['textExtra'] if 'hashtagName' in tag and len(tag['hashtagName'])>0]
  else:
      to_return['hashtag'] = []
  if 'challenges' in tiktok_dict:
      to_return['challenges'] = [{k : challenge[k]} for k in ('id', 'title', 'desc', 'isCommerce')for challenge in tiktok['challenges']]
  else:
      to_return['challenges'] = []
  return to_return

items = list()
cursor = videos_collection.find()
stored = set([entry['_id'] for entry in cursor])

with open('videos.txt') as f:
    lines = f.readlines()
    for line in tqdm.tqdm(lines):
        try:
            context = eval(line)
            if context['id'] in stored: continue
            context['_id'] = context.pop('id')
            stored.add(context['_id'])
            items.append(context['_id'])
        except KeyboardInterrupt:
            if items:
                videos_collection.insert_many(items)

print(items)
if items:
    videos_collection.insert_many(items)