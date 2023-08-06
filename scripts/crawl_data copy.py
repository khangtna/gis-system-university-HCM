import googlemaps
import pandas as pd
import datetime

API_KEY = 'AIzaSyDg8jJg3x-HLGPJM4ayihCdsuQJj_YTdoo'

gmaps = googlemaps.Client(key=API_KEY)

places_result = gmaps.places(query='đại học tôn đức thắng', location='Ho Chi Minh City', radius=20000)
list_uni=[]
for place in places_result['results']:
    place_id = place['place_id']
    place_details = gmaps.place(place_id=place_id, fields=['name', 'formatted_address', 'geometry/location'])
    print(place_details)

    # Lấy thông tin chi tiết về địa điểm
    name = place_details['result']['name']
    address = place_details['result']['formatted_address']
    location = place_details['result']['geometry']['location']  

    id=0
    location_name='Ho Chi Minh'
    created_date = datetime.datetime.today()
    update_time = datetime.datetime.today()

    print("Tên trường:", name)
    print("Địa chỉ:", address)
    print("Kinh độ:", location['lng'])
    print("Vĩ độ:", location['lat'])
    print("location_name:", location_name)
    print("created_date:", created_date)
    print("update_time:",update_time)
    print("------------------------------------")

    list_uni.append([id,name,location['lng'],location['lat'], location_name, created_date,update_time,1,address])


df = pd.DataFrame(list_uni, columns=['school_code','name', 'longitude', 'latitude','location_name','created_date','update_time','status','address'])
df.to_csv('D:\Study\PTIT\Intern  project\scripts\data\data_uni.csv', index=False)