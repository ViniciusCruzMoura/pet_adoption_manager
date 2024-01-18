from django.urls import path

from . import views

app_name = 'management_system'
urlpatterns = [
    path('', views.index, name='index'),
]