from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Landing_Page_Information,Introduction_Video
from .serializers import LandingPageSerializer,IntroVideosSerializer


 #Landing Page stuff
class Landing(APIView):
    def get(self, request, format=None):
        land = Landing_Page_Information.objects.all()[0:4]
        serializer = LandingPageSerializer(land, many=True)
        return Response(serializer.data)


#Landing Page stuff
class Intovid(APIView):
    def get(self, request, format=None):
        intro = Introduction_Video.objects.all()[0:4]
        serializer = IntroVideosSerializer(intro, many=True)
        return Response(serializer.data)