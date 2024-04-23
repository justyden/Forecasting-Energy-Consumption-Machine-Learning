# consumption_forecast/urls.py

from django.urls import path
from .views import home, upload_csv, help, error, results

urlpatterns = [
    path('', home, name='home'),
    path('help/', help, name='help'),
    path('upload/', upload_csv, name='upload_csv'),
    path('results/', results, name='results'),  # URL for displaying results
    path('error/', error, name='error'),
]