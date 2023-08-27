from django.urls import path,include
from .views import RegisterView

from users import views


urlpatterns = [
    
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
    # path('send-email/',views.sendMail,name='send'),
    # path('create-students/',views.StudentCreate.as_view()),
    # path('student-profile/',StudentList.as_view(), name='stud-profile'),
    # path('check-regtt/',CheckRegistr.as_view()),
    # path('reset-password/',views.ResetPassword.as_view(),name='reset_password'),


    #third-party reset
    # path('password-reset/',include('django_rest_passwordreset.urls',namespace='password_reset')),
    
    
]