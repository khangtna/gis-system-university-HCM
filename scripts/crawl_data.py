import googlemaps
import pandas as pd
import datetime

API_KEY = 'my key'
gmaps = googlemaps.Client(key=API_KEY)

list_name=[
    'Trường ĐH An ninh Nhân dân',
    'Trường ĐH Bách Khoa(ĐHQG TP.HCM)',
    'Trường ĐH Công nghiệp Thực phẩm',
    'Trường ĐH Công nghiệp TP.HCM',
    'Trường ĐH Công nghệ Thông tin (ĐHQG TP.HCM)',
    'Trường ĐH Cảnh sát Nhân dân',
    'Trường ĐH Giao thông Vận tải Phân hiệu tại TP.HCM',
    'Trường ĐH Giao thông Vận tải TP.HCM',
    'Trường ĐH Khoa học Tự nhiên (ĐHQG TP.HCM)',
    'Trường ĐH Khoa học Xã hội và Nhân văn (ĐHQG TP.HCM)',
    'Trường ĐH Kinh tế Luật (ĐHQG TP.HCM)',
    'Trường ĐH Kinh tế TP.HCM',
    'Trường ĐH Kiến Trúc TP.HCM',
    'Trường ĐH Lao động Xã hội cơ sở 2',
    'Trường ĐH Luật TP.HCM',
    'Đại học Mở',
    'Đại học Mỹ thuật TP.HCM',
    'Đại học Ngoại thương Cơ sở 2',
    'Đại học Ngân hàng TP.HCM',
    'Đại học Nông Lâm TP.HCM',
    'Phân hiệu Đại học Nội vụ Hà Nội',
    'Đại học Quốc tế (ĐHQG TP.HCM)',
    'Đại học Sân khấu  Điện ảnh TP.HCM',
    'Đại học Sư phạm Kỹ thuật TP.HCM',
    'Đại học Sư phạm Thể dục Thể thao',
    'Đại học Sư phạm TP.HCM',
    'Đại học Thể dục Thể thao TP. HCM',
    'Đại học Thủy lợi cơ sở 2',
    'Đại học Trần Đại Nghĩa',
    'Đại học Tài chính - Marketing',
    'Đại học Tài nguyên - Môi trường',
    'Đại học Tôn Đức Thắng',
    'Đại học Việt Đức',
    'Đại học Văn hóa TP.HCM',
    'Đại học Y Dược TP.HCM',
    'Đại học Y khoa Phạm Ngọc Thạch',
    'Khoa Y (ĐHQG TP.HCM)',
    'Khoa Chính trị - Hành chính (ĐHQG TP.HCM)',
    'Học viện Cán bộ TP.HCM',
    'Học viện Công nghệ Bưu chính Viễn thông cơ sở miền nam',
    'Học viện Hàng không Việt Nam',
    'Học viện Hành chính cơ sở phía Nam',
    'Học viện Kỹ thuật Mật mã cơ sở phía Nam',
    'Học viện Kỹ thuật Quân sự cơ sở 2',
    'Nhạc viện',
    'Phân viện miền Nam Học viện Thanh thiếu niên Việt Nam',
    'Đại học Công nghệ TP.HCM',
    'Đại học Công nghệ Sài Gòn',
    'Đại học Gia Định',
    'Đại học Văn Lang',
    'Đại học FPT',
    'Đại học Hoa Sen',
    'Đại học Hùng Vương',
    'Đại học Kinh tế - Tài chính',
    'Đại học Ngoại ngữ - Tin học',
    'Đại học Nguyễn Tất Thành',
    'Đại học Quốc tế Hồng Bàng',
    'Đại học Quốc tế Sài Gòn',
    'Đại học Văn Hiến',
    'Đại học RMIT Việt Nam',
    'Đại học Fulbright Việt Nam',
    'Đại học Fulbright Việt Nam',
    'Đại học Swinburne Vietnam (Cơ sở TP.HCM)'
]
list_uni=[]
id=0
for uni in list_name:
    places_result = gmaps.places(query=uni, location='Ho Chi Minh City', radius=20000)
    for place in places_result['results']:
        place_id = place['place_id']
        place_details = gmaps.place(place_id=place_id, fields=['name', 'formatted_address', 'geometry/location'])
        
        # Lấy thông tin chi tiết về địa điểm
        name = place_details['result']['name']
        address = place_details['result']['formatted_address']
        location = place_details['result']['geometry']['location']  
        id+=1
        location_name='Ho Chi Minh'
        created_date = datetime.datetime.today()
        update_time = datetime.datetime.today()
        print("ID:", id)
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