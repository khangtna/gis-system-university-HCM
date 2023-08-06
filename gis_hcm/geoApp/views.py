from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib import messages
import folium

from .models import SchoolDetail, GeoCode, Majors, SchoolMajors

# Create your views here.

def home(request):

    m = folium.Map(location=[10.8231, 106.6297],zoom_start=12)
    majors = Majors.objects.filter(status= True)
    majors_name="Chưa chọn chuyên ngành"

    # search
    if 'search_query' in request.GET and request.GET['search_query'].strip():
        search_query = request.GET['search_query']
        name_school = SchoolDetail.objects.filter(name__icontainsw=search_query)
        geo_code_count = name_school.count
        # print(name_school)
        for i in name_school:
            geo_code = GeoCode.objects.filter(school_code= i)
            # print(geo_code)
            for j in geo_code:
                folium.Marker([j.latitude, j.longitude], popup= j.school_code.name,icon=folium.Icon()).add_to(m)
    elif 'quanhuyen' in request.GET and request.GET['quanhuyen'].strip():
        search_query = request.GET['quanhuyen']
        name_school = SchoolDetail.objects.filter(address__icontains=search_query)
        geo_code_count = name_school.count
        # print(name_school)
        for i in name_school:
            geo_code_1 = GeoCode.objects.filter(school_code= i)
            # print(geo_code)
            for j in geo_code_1:
                folium.Marker([j.latitude, j.longitude], popup= j.school_code.name,icon=folium.Icon()).add_to(m)
    elif 'majors' in request.GET and request.GET['majors'].strip():
        search_query = request.GET['majors']
        school_majors = SchoolMajors.objects.filter(majors_code=search_query)
        school_codes = school_majors.values_list('school_code', flat=True)
        name_school = SchoolDetail.objects.filter(school_code__in=school_codes)
        # print(name_school)
        majors_name = Majors.objects.filter(majors_code= search_query).values_list('majors_name', flat=True)[0]
        geo_code_count = name_school.count
        for i in name_school:
            geo_code = GeoCode.objects.filter(school_code= i.school_code)
            for j in geo_code:
                folium.Marker([j.latitude, j.longitude], popup= j.school_code.name,icon=folium.Icon()).add_to(m) 
    else:
        name_school = SchoolDetail.objects.filter(status= True)
        geo_code = GeoCode.objects.filter(status= True)
        geo_code_count = geo_code.count
        for i in geo_code:
            folium.Marker([i.latitude, i.longitude], popup= i.school_code.name,icon=folium.Icon()).add_to(m)

    m=m._repr_html_()

    context={
        'my_map': m,
        'school_detail': name_school,
        'geo_code_count':geo_code_count,
        'majors':majors,
        'majors_name': majors_name
        }
    return render(request,'home.html',context)

