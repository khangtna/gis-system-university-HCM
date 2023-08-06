GIS system of university at HCM
-------------------------

how to run
------------
  * cd gis_hcm
  * pip install -r requirements.txt\
   ***or*** python -m pip install -r requirements.txt 
  * Config database \gis_hcm\settings.py
  * database database/sqldb-geolocation.bak (import SQL Server)
  * python manage.py createsuperuser
  * python manage.py makemigrations
  * python manage.py migrate
  * python manage.py runserver
