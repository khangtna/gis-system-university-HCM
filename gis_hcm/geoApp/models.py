from django.db import models

# Create your models here.

class SchoolDetail(models.Model):
    school_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    address = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    location_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_date = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return str(self.school_code)
    
    class Meta:
        managed = False
        db_table = 'school_detail'
    
    


class EmployeeDetail(models.Model):
    emp_code = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    lastname = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    address = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    numberphone = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_detail'


class GeoCode(models.Model):
    location_code = models.IntegerField(primary_key=True)
    school_code = models.ForeignKey(SchoolDetail, models.DO_NOTHING, db_column='school_code')
    emp_code = models.ForeignKey(EmployeeDetail, models.DO_NOTHING, db_column='emp_code')
    longitude = models.FloatField()
    latitude = models.FloatField()
    location_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_date = models.DateTimeField()
    update_time = models.DateTimeField()
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'geo_code'


class Majors(models.Model):
    majors_code = models.AutoField(primary_key=True)
    majors_name = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'majors'


class SchoolMajors(models.Model):
    school_code = models.ForeignKey(SchoolDetail, models.DO_NOTHING, db_column='school_code')
    majors_code = models.ForeignKey(Majors, models.DO_NOTHING, db_column='majors_code')

    class Meta:
        managed = False
        db_table = 'school_majors'

