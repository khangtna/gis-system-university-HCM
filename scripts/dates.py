import datetime

# ngay_hien_tai = datetime.date.today()
# print(ngay_hien_tai)
# ngay_hien_tai_dinh_dang = ngay_hien_tai.strftime("%d/%m/%Y")
# print(ngay_hien_tai_dinh_dang)

# timestamp = datetime.datetime.today().timestamp()
# print(timestamp)

import datetime

ngay_gio_hien_tai = datetime.datetime.now()
print(ngay_gio_hien_tai)
ngay_gio_dinh_dang = ngay_gio_hien_tai.strftime("%d/%m/%Y %H:%M:%S")
print(ngay_gio_dinh_dang)