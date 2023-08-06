from django.contrib import admin

from .models import SchoolDetail, GeoCode,EmployeeDetail,Majors,SchoolMajors

# Register your models here.

admin.site.register(SchoolDetail)
admin.site.register(EmployeeDetail)
admin.site.register(GeoCode)
admin.site.register(Majors)
admin.site.register(SchoolMajors)

