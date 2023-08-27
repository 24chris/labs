
from rest_framework import serializers

from .models import Landing_Page_Information,Introduction_Video

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing_Page_Information
        fields = ('id','why_field','about_intern','about_supervision','about_skills','about_solutions','about_us','about_views','follow_us','contact_us','pricing','demo','partners','slug')



class IntroVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction_Video
        fields = ('id','name','video_link','slug')