
import imp
from django.urls import path, include
from .views import Landing,Intovid

from content import views

urlpatterns = [
    path('home-page/',views.Landing.as_view()),
    path('intro-videos/',views.Intovid.as_view()),

       
]