from dataclasses import field, fields

from rest_framework import serializers

from .models import Course,Lesson,Module

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id','name','slug','description','get_absolute_url','video_url')


class ModuleSerializer(serializers.ModelSerializer):
    module_lesson = LessonSerializer(many=True)
    
    class Meta:
        model = Module
        fields = ('id','name','slug','description','get_absolute_url','module_lesson')


class CourseSerializer(serializers.ModelSerializer):
    course_module = ModuleSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id','name','slug','get_absolute_url','description','level','course_module')




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