from django.urls import path
from . import views


app_name = 'cms'

urlpatterns = [
    path('', views.hagurumasite, name='haguruma_site'),
]
