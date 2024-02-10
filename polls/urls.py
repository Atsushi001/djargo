from django.urls import path
from . import views, fun


urlpatterns = [
    path('', views.index, name ='index'),
    path('fun/', fun.index, name = 'fun'),
]