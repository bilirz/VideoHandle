from function import *

count_time = time.strftime('%Y-%m-%d %H:%M:%S')
for up in dbf.find():
    info = json.loads(get_response(f"https://api.bilibili.com/x/space/wbi/acc/info?mid={up['mid']}").text)
    images = get_response(f"{info['data']['face']}").content
    with open(f"E:\\Progress\\anicharts\\static\\images\\{up['mid']}.jpg", 'wb') as f:
        f.write(images)
        print(f"获取了{up['mid']}")
    time.sleep(1)
