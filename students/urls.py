from django.urls import path
from .views import StudentCreate,CheckRegistration,ChosenCourse

from students import views


urlpatterns = [

    # path('mail/test/send/email/',views.sendMail,name='send'),
    path('new/student/detail/create-students/',StudentCreate.as_view()),
    path('reg/new/register/check-reg/',CheckRegistration.as_view()),
    path('course/list/reg/chosen-course/',ChosenCourse.as_view()),
    
]