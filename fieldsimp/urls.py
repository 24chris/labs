from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView
from users.views import RegisterView

from rest_framework_simplejwt.views import ( 
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/',include('djoser.urls')),
    # path('auth/',include('djoser.urls.authtoken')),
    # path('auth/',include('djoser.urls.jwt')),
        
    #Auth api's
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),

    
    #Index Content
    path('api/v1/',include('content.urls')),

    #Course
    path('api/v1/',include('course.urls')),

    #Students
    path('api/v1/',include('students.urls')),

    #Non-Students
    path('api/v1/',include('nonStudents.urls')),

    #LogBook
    path('api/v1/',include('logbook.urls')),

    #Payments
     path('api/v1/',include('payments.urls')),

     #Index Content
    path('api/v6/',include('users.urls')),


     #Flutterwave
    #  path("djangoflutterwave/", include("djangoflutterwave.urls", namespace="djangoflutterwave"))


    
    

    # Local Reviews add
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/user/', views.UserAPIView.as_view(), name='login'),
    # path('api/register/', views.RegisterUserAPIView.as_view(), name='register')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


                   