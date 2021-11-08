import multiprocessing
manager = multiprocessing.manager()
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
  to_return["duetEnabled"] = tiktok['duetEnabled']
  to_return["stitchEnabled"] = tiktok['stitchEnabled']
  to_return["shareEnabled"] = tiktok['shareEnabled']
  if 'textExtra' in tiktok:
      to_return['hashtag'] = [{k : tag[k]} for k in ('hashtagName', 'hashtagId', 'type', 'subType')for tag in tiktok['textExtra'] if 'hashtagName' in tag and len(tag['hashtagName'])>0]
  else:
      to_return['hashtag'] = []
  if 'challenges' in tiktok:
      to_return['challenges'] = [{k : challenge[k]} for k in ('id', 'title', 'desc', 'isCommerce')for challenge in tiktok['challenges']]
  else:
      to_return['challenges'] = []
  return to_return

items = list()
with open('videos.txt') as f:
    lines = f.readlines()
    for line in lines:
        context = eval(line)
        items.append(context)
        break
print(items)