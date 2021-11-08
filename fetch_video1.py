import pymongo
import pickle
import os
import multiprocessing
from TikTokApi import TikTokApi
from TikTokAPI import TikTokAPI
import tqdm
import requests
logname = os.path.basename(__file__) + '.log'

if os.path.exists(logname):
  os.remove(logname)

manager = multiprocessing.Manager()
# stopwordset = manager.dict({word : 0 for word in stopwords.words('english')})
# # 建立mongodb连接
client = pymongo.MongoClient(host='localhost', port=27017)

db = client.tiktok

# # 创建一个daily集合，类似于MySQL中“表”的概念
# group = db['group']

users_db = db.users
videos_db = db.videos
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKRED='\033[0;31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tokgreen(s):
    return bcolors.OKGREEN + s + bcolors.ENDC

def tokblue(s):
    return bcolors.OKBLUE + s + bcolors.ENDC

def tokred(s):
    return bcolors.OKRED + s + bcolors.ENDC

def tokwaring(s):
    return bcolors.WARNING + s + bcolors.ENDC
verifyfp = 'verify_kvpztceo_fB1ntLiL_DNSj_4adI_AtAd_UhrNf5vVNKWK'
api = TikTokApi.get_instance(custom_verifyFp=verifyfp,use_test_endpoint=True)
cookie = {
  "s_v_web_id": "verify_kvpygqgy_QL3BEdUe_St1p_4nCY_BAkF_ZvQWZ0Ryv9SD",
  "tt_webid": "k85EDzQ5zvrI0qA3TTJqcIKZOT"
}
 
from requests.structures import CaseInsensitiveDict

usid='MS4wLjABAAAA7CyNvLiT5-wfMyn7_KhW2jJM-QZZMgvDH9UjKnlgd2pCWpyI0PUewJn-f_hLOuMD'
url = f"https://api.tikapi.io/public/posts?secUid={usid}&count=30&cursor=0"

headers = CaseInsensitiveDict()
headers["X-API-KEY"] = "2kLb6QpCsSqXFcwP8mIUlZ4Aoymo1L2v"
headers["accept"] = "application/json"


resp = requests.get(url, headers=headers)

print(resp.status_code)
# api = TikTokAPI(cookie=cookie)
# user_obj = api.getUserByName("fcbarcelona")
# sys.exit()
def simple_dict(tiktok_dict):
  to_return = {}
#   to_return['author.uniqueId'] = tiktok_dict['author']['uniqueId']
#   to_return['author.id'] = tiktok_dict['author']['id']
#   to_return['id'] = tiktok_dict['id']
#   to_return['desc'] = tiktok_dict['desc']
#   to_return['createTime'] = tiktok_dict['createTime']
#   to_return['videoduration'] = tiktok_dict['video']['duration']
#   to_return['link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['author.uniqueId'], to_return['id'])
#   to_return['likes'] = tiktok_dict['stats']['diggCount']
#   to_return['stats.shareCount'] = tiktok_dict['stats']['shareCount']
#   to_return['stats.commentCount'] = tiktok_dict['stats']['commentCount']
#   to_return['stats.playCount'] = tiktok_dict['stats']['playCount']
#   to_return["duetEnabled"] = tiktok['duetEnabled']
#   to_return["stitchEnabled"] = tiktok['stitchEnabled']
#   to_return["shareEnabled"] = tiktok['shareEnabled']
#   if 'textExtra' in tiktok:
#       to_return['hashtag'] = [{k : tag[k]} for k in ('hashtagName', 'hashtagId', 'type', 'subType')for tag in tiktok['textExtra'] if 'hashtagName' in tag and len(tag['hashtagName'])>0]
#   else:
#       to_return['hashtag'] = []
#   if 'challenges' in tiktok:
#       to_return['challenges'] = [{k : challenge[k]} for k in ('id', 'title', 'desc', 'isCommerce')for challenge in tiktok['challenges']]
#   else:
#       to_return['challenges'] = []
  return to_return
with open('usernames.pkl', 'rb') as f:
    usernames = pickle.load(f)
print(len(usernames))
count=2000
videos= []
headers = ['author.uniqueId', 'author.id', 
        'id', 'desc', 'createTime', 
        'videoduration', 'link', 
        'likes', 'stats.shareCount', 
        'stats.commentCount', 
        'stats.playCount', 
        'duetEnabled',
        'stitchEnabled', 
        'shareEnabled']
for username in tqdm.tqdm(usernames[:3]):
    try:
        print(username)
        tiktoks = api.by_username(username, count=count)
    except :
        print(tokgreen('continue'))
        continue

    for tiktok in tiktoks:
        print(simple_dict(tiktok))
        videos.append(simple_dict(tiktok))
        # print(simple_dict(tiktok))
print(videos)
videos_db.insert_many(videos)