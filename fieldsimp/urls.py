from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from users import views
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import ( 
    TokenRefreshView,
)

# from course import urls
# from students import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
    # path('auth/',include('djoser.urls.jwt')),
    path('api/v1/',include('course.urls')),
    path('api/v1/',include('content.urls')),
    path('api/v1/',include('users.urls')),
    path('api/v1/',include('payments.urls')),
    

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/register/', RegisterView.as_view(), name='auth_register'),
    # path('api/v1/',include('users.py')),

    # Local Reviews add
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/user/', views.UserAPIView.as_view(), name='login'),
    # path('api/register/', views.RegisterUserAPIView.as_view(), name='register')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
