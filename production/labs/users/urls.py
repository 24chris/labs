from django.urls import path
from .views import RegisterView,sendMail,StudentCreate

from users import views


urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('send-email/',views.sendMail,name='send'),
    path('create-students/',views.StudentCreate.as_view()),
    
]