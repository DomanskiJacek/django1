from django.urls import path
from . import views

urlpatterns = [
    path('', views.rgann, name='rgann' ),
    path('rgann', views.rgann, name='rgann' ),
]