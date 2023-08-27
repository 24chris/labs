from ast import Mod
from urllib import response
from django.db.models import Q
from itertools import product
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from .models import Course,Module,Lesson,Comment
from .serializers import CourseSerializer,ModuleSerializer,LessonSerializer,CommentSerializer




####################### Courses ############################
#All the latest courses
class LatestCourseList(APIView):  
    def get(self, request, format=None):
        course = Course.objects.all()[0:4]
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)


# Specific course
class CourseDetail(APIView):

#     # permission_classes = [IsAuthenticated]

# #     def get(self,request):
# #         user = request.user
# #         course = Course.objects.filter(students=user)
# #         serializer = CourseSerializer(course)
# #         return Response(serializer.data)


    def get_object(self,course_slug):

        try:
            return Course.objects.get(slug=course_slug)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,course_slug,format=None):
        course = self.get_object(course_slug)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


####################### Modules ############################
# All the latest modules
class LatestModuleList(APIView):  
    def get(self, request, format=None):
        module = Module.objects.all()[0:4]
        serializer = ModuleSerializer(module, many=True)
        return Response(serializer.data)

# Specific module
class ModuleDetail(APIView):
    def get_object(self,course_slug,module_slug):
        try:
            return Module.objects.filter(course__slug=course_slug).get(slug=module_slug)
        except Module.DoesNotExist:
            raise Http404

    def get(self,request,course_slug,module_slug,format=None):
        module = self.get_object(course_slug,module_slug)
        serializer = ModuleSerializer(module)
        return Response(serializer.data)



####################### Lessons ############################
# All the lessons
class LatestLessonList(APIView):
    def get(self, request, format=None):
        lesson = Lesson.objects.all()[0:4]
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)


# Specific Lesson
class LessonDetail(APIView):
    def get_object(self, course_slug,module_slug,lesson_slug):
        try:
            return Lesson.objects.filter(course__slug=course_slug).get(module__slug=module_slug,slug=lesson_slug)
        except Lesson.DoesNotExist:
            raise Http404
    
    def get(self,request,course_slug,module_slug,lesson_slug,format=None):
        lesson = self.get_object(course_slug,module_slug,lesson_slug)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
        

####################### Comments ############################
# Add the comments to a lesson
class AddComment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request,lesson_slug,format=None, *args, **kwargs):
        try:
            lesson=Lesson.objects.get(lesson_slug=lesson_slug)
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        content=json.loads(request.body)

        if not content.get('message'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CommentSerializer(data=content)

        if serializer.is_valid():
            comment=serializer.save(user=request.user)

            lesson.comment.add(comment)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

