import imp
from django.urls import path, include
from .views import webhook

from payments import views

urlpatterns = [
    path('webhooks/flutterwave/',views.webhook,name='webhook'),

    
       
]