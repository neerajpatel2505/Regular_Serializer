
from django.urls import path
from .views import *

urlpatterns = [
    path("stu_info/<int:pk>",student_detail,name='name'),
    path("stu_list/",student_list,name='student_list'),
    path('list/',list,name='list'),
]