from django.urls import path
from .views import LogBookCreate
from students import views


urlpatterns = [
    path('new/student/logbook/logbook-create/',LogBookCreate.as_view(),name='logbook'),
    
]