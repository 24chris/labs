# from ast import Mod
# from urllib import response
# from django.db.models import Q
# from itertools import product
# from django.http import Http404

# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status,permissions
# from rest_framework.permissions import IsAuthenticated
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse

# from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import Course,Module,Lesson
# from .serializersOLD import CourseSerializer,ModuleSerializer,LessonSerializer,EnrolledSerializer,CommentSerializer

# import re
# import json




# #Encode the url of the video added
# def embed_url(videoUrl):
#         regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"

#         return re.sub(regex, r"https://www.youtube.com/embed/\1",videoUrl)



# #Check if a course has been paid for or not
# class CourseStudy(APIView):

#     # def get_object(self,course_slug):
#     #     try:
#     #         return Course.objects.get(slug=course_slug)
#     #     except Course.DoesNotExist:
#     #         raise Http404

#     def get(self,request,format=None):
        
                
#         return Response('We got here!')


# # All chosen lessons
# class LatestLessonList(APIView):
#     def get(self, request, format=None):
#         # if Lesson.video_url == "":
#         #     Lesson.video_url = None
#         # #change the url's video to embed_url
#         # if Lesson.video_url != None:
#         #     Lesson.video_url = embed_url(Lesson.video_url)
#         lesson = Lesson.objects.all()[0:4]
#         serializer = LessonSerializer(lesson, many=True)
#         return Response(serializer.data)

# # All the latest modules
# # class LatestModuleList(APIView):  
# #     def get(self, request, format=None):
# #         module = Module.objects.all()
# #         serializer = ModuleSerializer(module, many=True)
# #         return Response(serializer.data)

# #All the latest courses
# class LatestCourseList(APIView):  
#     def get(self, request, format=None):
#         course = Course.objects.all()[0:4]
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)

# #Individual course
# class CourseDetail(APIView):

# #     # permission_classes = [IsAuthenticated]

# # #     def get(self,request):
# # #         user = request.user
# # #         course = Course.objects.filter(students=user)
# # #         serializer = CourseSerializer(course)
# # #         return Response(serializer.data)


#     def get_object(self,course_slug):

#         try:
#             return Course.objects.get(slug=course_slug)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self,request,course_slug,format=None):
#         course = self.get_object(course_slug)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

# #That one course
# class EnrollChosen(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         user = request.user
#         course = Course.objects.filter(enrolled_course=user)
#         # course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)


# # Individual module
# class ModuleDetail(APIView):
#     def get_object(self,course_slug,module_slug):
#         try:
#             return Module.objects.filter(course__slug=course_slug).get(slug=module_slug)
#         except Module.DoesNotExist:
#             raise Http404

#     def get(self,request,course_slug,module_slug,format=None):
#         module = self.get_object(course_slug,module_slug)
#         serializer = ModuleSerializer(module)
#         return Response(serializer.data)

# #Individual Lesson
# class LessonDetail(APIView):
#     def get_object(self, course_slug,module_slug,lesson_slug):
#         try:
#             return Lesson.objects.filter(course__slug=course_slug).get(module__slug=module_slug,slug=lesson_slug)
#         except Lesson.DoesNotExist:
#             raise Http404
    
#     def get(self,request,course_slug,module_slug,lesson_slug,format=None):
#         lesson = self.get_object(course_slug,module_slug,lesson_slug)
#         serializer = LessonSerializer(lesson)
#         return Response(serializer.data)
        
            

# #Enroll for course

# def enroll(request):
#     if request.method == "POST":
#         user = request.user
#         course_slug = request.POST["course_slug"]

#         course = Course.objects.get(slug=course_slug)

#         # if the user is not enrolled, the user is routed to the course page
#         try:
#             enroll = Enrolled.objects.get(course=course, user=user)
#             return HttpResponseRedirect(reverse("course", args=(course_slug,)))
#         except Enrolled.DoesNotExist:
#             enroll = Enrolled(user=user, course=course)
#             enroll.save()
#             return HttpResponseRedirect(reverse("course", args=(course_slug,)))


# class EnrollToCourse(APIView):
#     def enrollment(self,request,format=None,*args,**kwargs):
#         if request.method =="POST":
#             course_slug = request.POST['course_slug']
#             user = request.user
#             course = Course.objects.get(slug=course_slug)
#             course.students.add(user)
#             course.save()
#             return Response('You enrolled')
#         else:
#             return Response('Not enrolled')




# class Dashboard(APIView):
#     def get_object(self, course_slug,user,request):
#         try:
#             return Course.objects.filter(course__slug=course_slug).get(user=request.user)
#         except Course.DoesNotExist:
#             raise Http404
    
#     def get(self,request,course_slug,user,format=None):
#         selected_course = self.get_object(course_slug,user=user)
#         serializer = CourseSerializer(selected_course)
#         return Response(serializer.data)





# #enroll or return all students and non-students registered for a course
# # class EnrollCategorylist(APIView):
# #     def get(self,request,format=None):






# # class LessonDetail(APIView):
# #     def get_object(self,category_slug,lesson_slug):
# #         try:
# #             return Lesson.objects.filter(category_slug=category_slug).get(slug=lesson_slug)
# #         except Lesson.DoesNotExist:
# #             raise Http404
    
# #     def get(self,request,category_slug,lesson_slug,format=None):
# #         lesson = self.get_object(category_slug,lesson_slug, lesson_slug)
# #         serializer = LessonSerializer(lesson)
# #         return Response(serializer.data)

# # class CourseDetail(APIView):
# #     def get_object(self, category_slug,course_slug):
# #         try:
# #             return Course.objects.get(category_slug=category_slug).get(slug=course_slug)
# #         except Course.DoesNotExist:
# #             raise Http404

# #     def get(self,request,category_slug,course_slug,format=None):
# #         course = self.get_object(category_slug, course_slug)
# #         serializer = CourseSerializer(course)
# #         return Response(serializer.data)




























# # class CourseListView(ListView):
# #     model = Course


# # class CourseDetailView(DetailView):
# #     model = Course


# # class LessonDetailView(LoginRequiredMixin, View):

# #     def get(self, request, course_slug, lesson_slug, *args, **kwargs):
# #         course = get_object_or_404(Course, slug=course_slug)
# #         lesson = get_object_or_404(Lesson, slug=lesson_slug)
# #         user_membership = get_object_or_404(UserMembership, user=request.user)
# #         user_membership_type = user_membership.membership.membership_type
# #         course_allowed_mem_types = course.allowed_memberships.all()
# #         context = { 'object': None }
# #         if course_allowed_mem_types.filter(membership_type=user_membership_type).exists():
# #             context = {'object': lesson}
# #         return render(request, "courses/lesson_detail.html", context)


# # Add Comment To course
# class AddComment(APIView):
#     permission_classes=[IsAuthenticated]
#     def post(self,request,course_slug,*args, **kwargs):
#         try:
#             course=Course.objects.get(course_slug=course_slug)
#         except Course.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         content=json.loads(request.body)

#         if not content.get('message'):
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
#         serializer = CommentSerializer(data=content)

#         if serializer.is_valid():
#             comment=serializer.save(user=request.user)

#             course.comment.add(comment)

#             return Response(status=status.HTTP_200_OK)

#         else:
#             return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)