import pymongo
import tqdm
import pandas as pd
import argparse
import logging
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.tiktok
class ColoredLogger(logging.Logger):
    FORMAT = "[$BOLD%(name)-20s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"
    COLOR_FORMAT = formatter_message(FORMAT, True)
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)                

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


logging.setLoggerClass(ColoredLogger)

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
all_videos = list(videos_collection.find({'author.id': {'$in': list(verified_user)}}))
logging.info(f'There are {len(all_videos)} videos and {len(verified_user)} verified users.')
for entry in tqdm.tqdm(all_videos):
    dic = simple_dict(dict(entry))
    content.append([dic[k] for k in headers])
df = pd.DataFrame(columns=headers, data=content)
df.to_csv('videos_dataset.csv', index=False)

