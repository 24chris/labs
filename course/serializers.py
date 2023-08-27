from dataclasses import field, fields
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Course,Lesson,Module,Comment
from users.serializers import UserSerializer

User = get_user_model()


# Lesson Serializer
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','name','module','slug','description','get_absolute_url','video_url','lesson_uuid','created_at')

# Module Serializer
class ModuleSerializer(serializers.ModelSerializer):
    module_lesson = LessonSerializer(many=True)
    
    class Meta:
        model = Module
        fields = ('id','name','course','slug','description','get_absolute_url','module_uuid','created_at','module_lesson')

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    course_module = ModuleSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id','name','course_category','slug','get_absolute_url','description','course_level','price','course_uuid','course_module')

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','message','created')