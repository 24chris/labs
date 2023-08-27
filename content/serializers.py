
from rest_framework import serializers

from .models import Landing_Page_Information,Introduction_Video

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing_Page_Information
        fields = ('id','information_name','information_description')



class IntroVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction_Video
        fields = ('id','name','video_link','slug')