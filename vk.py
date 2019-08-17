import vk_api
from datetime import datetime
import time
def main(time):

    login, password = '79013479188', 'RGMaster42'
    vk_session = vk_api.VkApi(login, password)
    

    
    vk_session.auth()
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)

    pyt = f'C:\\Users\\yrom1\\Desktop\\vk\\time_images\\{time}.jpg'

    photo = vk.photos.get(album_id='profile', rev=1)
    ph_id = photo['items'][0]['id']
    vk.photos.delete(photo_id=ph_id)

    upload.photo_profile(  
        pyt,
        owner_id=475045016
    )

    id = vk.wall.get(count=1)
    i = id['items'][0]['id']
    vk.wall.delete(post_id=i)


date = datetime.now()
d = date.strftime('%H%M')
while True:
    pro = datetime.now()
    v = pro.strftime('%H%M')
    if v != d:
        main(v)
        date = datetime.now()
        d = date.strftime('%H%M')
        time.sleep(40)
    else:
        time.sleep(5)


        
    


    