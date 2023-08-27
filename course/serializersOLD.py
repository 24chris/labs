# from dataclasses import field, fields

# from django.contrib.auth import get_user_model

# from rest_framework import serializers

# from .models import Course,Lesson,Module,Enrolled,Comment
# from users.serializers import UserSerializer

# User = get_user_model()

# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ('id','name','module','slug','description','get_absolute_url','video_url','lesson_uuid','created_at')


# class ModuleSerializer(serializers.ModelSerializer):
#     module_lesson = LessonSerializer(many=True)
    
#     class Meta:
#         model = Module
#         fields = ('id','name','course','slug','description','get_absolute_url','module_uuid','created_at','module_lesson')


# class CourseSerializer(serializers.ModelSerializer):
#     course_module = ModuleSerializer(many=True)

#     class Meta:
#         model = Course
#         fields = ('id','name','course_category','slug','get_absolute_url','description','course_level','price','course_uuid','course_module')



# class EnrolledSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
    
#     class Meta:
#         model = Enrolled
#         fields = ('id','user','course','date_enrolled')


# class CommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Comment
#         fields = ('id','user','message','created')











# class CommentSerializer(serializers.ModelSerializer):
#     # user = UserCreateSerializer(many=True)

#     class Meta:
#         model = Category
#         fields = ('id','user','message','created')





# New API's

# class LessonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lesson
#         fields = ('id','name','instruments','length','video_url')



# class CourseSerializer(serializers.ModelSerializer):
#     course = LessonSerializer(many=True)

#     class Meta:
#         model = Course
#         fields = ('id','name','get_absolute_url','description','instructed_by')


# class CategorySerializer(serializers.ModelSerializer):
#     category = CourseSerializer(many=True)

#     class Meta:
#         model = Category
#         fields = ('id','name','get_absolute_url')