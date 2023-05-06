from .views import *
from django.urls import path
'''
urlpatterns = [
    path('', home, name='home')
]
'''
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    #path("", home, name='home'),
    path("accessibilite/", views.accessibility_view, name="accessibilite"),
]
