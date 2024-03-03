from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('base', views.show_list, name='base'),
    path('ttt', views.ttt, name='ttt'),
    path('not', views.not_implemented, name='not_implemented'),
    path('si', views.simple, name='simple'),
    path('simple', views.simple, name='simple'),
    path('countries', views.countries, name='countries'),
    path('rgann/', include('rgapp.urls')),
]
