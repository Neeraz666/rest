from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('generic-student/', StudentGeneric.as_view(), name='genericstudents'),
    path('generic-studentUpdate/', StudentUpdateGeneric.as_view(), name='genericstudentsupdate'),
    path('student/', StudentAPI.as_view(), name='poststudent'),
    path('getbook/', get_book, name='getbook'),
    path('register/', RegisterUser.as_view(), name='registeruser'),
]