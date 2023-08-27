from ast import Mod
from urllib import response
from django.db.models import Q
from itertools import product
from django.http import Http404
import course

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Course,Module,Lesson
from .serializers import CourseSerializer,LessonSerializer,ModuleSerializer

import re




#Encode the url of the video added
def embed_url(video):
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"

        return re.sub(regex, r"https://www.youtube.com/embed/\1",video)


# All chosen lessons
class LatestLessonList(APIView):
    def get(self, request, format=None):
        lesson = Lesson.objects.all()[0:4]
        serializer = LessonSerializer(lesson, many=True)
        return Response(serializer.data)

#All the latest courses
class LatestCourseList(APIView):  
    def get(self, request, format=None):
        course = Course.objects.all()[0:4]
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

#All the latest modules
class LatestModuleList(APIView):  
    def get(self, request, format=None):
        module = Module.objects.all()[0:4]
        serializer = ModuleSerializer(module, many=True)
        return Response(serializer.data)

#Individual course
# class CourseDetail(APIView):
#     def get_object(self, course_slug):
#         try:
#             return Course.objects.get(slug=course_slug)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self,request,course_slug,format=None):
#         course = self.get_object(course_slug)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#Individual module
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

#Individual Lesson
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
        # try:
        #     lesson.video = embed_url(lesson.video)
        # except:
        #     lesson.video = None
            
        









#enroll or return all students and non-students registered for a course
# class EnrollCategorylist(APIView):
#     def get(self,request,format=None):






# class LessonDetail(APIView):
#     def get_object(self,category_slug,lesson_slug):
#         try:
#             return Lesson.objects.filter(category_slug=category_slug).get(slug=lesson_slug)
#         except Lesson.DoesNotExist:
#             raise Http404
    
#     def get(self,request,category_slug,lesson_slug,format=None):
#         lesson = self.get_object(category_slug,lesson_slug, lesson_slug)
#         serializer = LessonSerializer(lesson)
#         return Response(serializer.data)

# class CourseDetail(APIView):
#     def get_object(self, category_slug,course_slug):
#         try:
#             return Course.objects.get(category_slug=category_slug).get(slug=course_slug)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self,request,category_slug,course_slug,format=None):
#         course = self.get_object(category_slug, course_slug)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)




























# class CourseListView(ListView):
#     model = Course


# class CourseDetailView(DetailView):
#     model = Course


# class LessonDetailView(LoginRequiredMixin, View):

#     def get(self, request, course_slug, lesson_slug, *args, **kwargs):
#         course = get_object_or_404(Course, slug=course_slug)
#         lesson = get_object_or_404(Lesson, slug=lesson_slug)
#         user_membership = get_object_or_404(UserMembership, user=request.user)
#         user_membership_type = user_membership.membership.membership_type
#         course_allowed_mem_types = course.allowed_memberships.all()
#         context = { 'object': None }
#         if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
#             context = {'object': lesson}
#         return render(request, "courses/lesson_detail.html", context)