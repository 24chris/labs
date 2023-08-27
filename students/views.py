from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from rest_framework import generics
from django.urls import reverse
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import StudentSerializer
from .models import StudentProfile

from users.models import UserAccount


User = get_user_model()


# Send registered user mail
# def sendMail(request):
#     template = render_to_string('letter.html', {'university':request.user.username})
#     email = EmailMessage(
#         'Intern Letter from Student App',
#         template,
#         'ictlabs@example.com',
#         ['mark@example.com'],
#     )
#     email.send()

#     return Response({"Email sent successfully": "Some more"})


#Complete student registration
class StudentCreate(APIView):

    permission_classes = [IsAuthenticated]

    # def sendMail(request):
    #     template = render_to_string('letter.html', {'student':request.user.username})
    #     email = EmailMessage(
    #         'Intern Letter from Student App',
    #         template,
    #         'ictlabs@example.com',
    #         ['mark@example.com'],
    #     )
    #     print("details\n******",request.user.username)
    #     email.send()


    #     return Response({"Email sent successfully": "Some more"})

    def post(self, request,format=None, *args, **kwargs):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student_instance = student.save(user=request.user)
            # student_instance.registered = True
            # self.sendMail(student_instance)
            # print(student.data)
            # print("huio",student_instance.university)
            return Response(student.data, status=status.HTTP_201_CREATED)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    # def check_student_registration(request):
    #     try:
    #         student = StudentProfile.objects.get(user=request.user)
    #         return 'Mehn you registred'
    #     except student.DoesNotExist:
    #         return 'Men you register'

class ChosenCourse(APIView):
    permission_classes = [IsAuthenticated]

    # def get(self,request,format=None,*args,**kwargs):
    #     try:
    #         course = StudentProfile.objects.filter(user=request.user)
    #         serializer = StudentSerializer(course)
    #         return Response(course.data,status=status.HTTP_200_OK)
    #     except course.DoesNotExist:
    #         return Response('You have not chosen a course') 
    def get_object(self,request,univeristy):
        try:
            return StudentProfile.objects.filter(univeristy=univeristy)
        except StudentProfile.DoesNotExist:
            raise Http404
        
    def get(self,university,format=None):
        cr_person = self.get_object(university)
        serializer = StudentSerializer(cr_person)
        return Response(serializer.data)
    
            

class CheckRegistration(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,format=None,*args,**kwargs):
        try:
            student = StudentProfile.objects.get(user=request.user)
            return Response('Man you registred')
        except student.DoesNotExist:
            return Response('Register Please')





# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def studentCreate(request):
#         student = StudentSerializer(data=request.data)
#         if student.is_valid():
#             student.save(user=request.user)
#             sendMail(request)
#             return Response(student)
#         return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)



