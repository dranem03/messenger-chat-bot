from googleapiclient.discovery import build
from cachetools import TTLCache
cacher = TTLCache(maxsize=512, ttl=100)





service = build("customsearch", "v1", developerKey="YOUR_GOOGLE_DEVELOPER_KEY_HERE")

mycx = "YOUR_CX_HERE"

"""
global larawan

larawan = []
"""

def google_img(recipient_id, to_search, res_qty):
    global res
    cacher['{}_result_cache'.format(recipient_id)] = []
    res = service.cse().list(
        q = to_search,
        cx = mycx,
        searchType = 'image',
        num = int(res_qty),
        #imgType = 'photo',
        fileType = 'jpg',
        safe = 'off'
    ).execute()

#google_img("sports car wallpaper", 3)

    if not 'items' in res:
        cacher['{}_result_cache'.format(recipient_id)].clear()
        cacher['{}_result_cache'.format(recipient_id)].append("sorry_not_found")
        cacher['{}_result_cache'.format(recipient_id)].append("https://dubsism.files.wordpress.com/2017/12/image-not-found.png")
        #print('No result!!\nres is: {}'.format(res))
    else:
        cacher['{}_result_cache'.format(recipient_id)].clear()
        for item in res['items']:
            cacher['{}_result_cache'.format(recipient_id)].append(item['link'])
            
            print('==============================')
            #print(str(item['title']))
            print(item['link'])
            
#google_img("hacker mode", 2)

for i in larawan:
    print(i)



def more_img(recipient_id, to_search, res_qty):
    global res
    
    qwerty = int(res_qty) - 10
    google_img(recipient_id, to_search, 10)
    res = service.cse().list(
        q = to_search,
        cx = mycx,
        searchType = 'image',
        num = qwerty,
        imgType = 'photo',
        fileType = 'jpg',
        safe = 'off',
        start = 10
    ).execute()

#google_img("sports car wallpaper", 3)

    if not 'items' in res:
        cacher['{}_result_cache'.format(recipient_id)].clear()
        cacher['{}_result_cache'.format(recipient_id)].append("sorry_not_found")
        cacher['{}_result_cache'.format(recipient_id)].append("https://dubsism.files.wordpress.com/2017/12/image-not-found.png")
        #print('No result!!\nres is: {}'.format(res))
    else:
        for item in res['items']:
            cacher['{}_result_cache'.format(recipient_id)].append(item['link'])



