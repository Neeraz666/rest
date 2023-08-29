from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.post_student, name='poststudent'),
    path('updatestudent/<id>', views.update_student, name='updatestudent'),
    path('deletestudent/<id>', views.delete_student, name='deletestudent'),
    path('getbook', views.get_book, name='getbook'),
]