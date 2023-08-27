from django.urls import path
from .views import NonStudentCreate

from nonStudents import views


urlpatterns = [

    path('non/student/send/email/',views.sendMail,name='send'),
    path('choose/create/non/students/',NonStudentCreate.as_view()),
           
]