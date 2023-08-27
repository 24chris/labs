from .serializers import UserCreateSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

#reset password imports
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.generics import GenericAPIView



from users.models import UserAccount


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer


# Send registered user mail
# def sendMail(request):
#     template = render_to_string('letter.html', {'name': request.user.username})
#     email = EmailMessage(
#         'Intern Letter from User App',
#         template,
#         'ictlabs@example.com',
#         ['mark@example.com'],
#     )
#     email.send()

#     return Response({"Email sent successfully": "Some more"})


# class ResetPassword(GenericAPIView):
#     def post(self,request,**args,**kwargs):
#         email = request.data.get('email',None)
#         password = request.data.get('password',None)
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'error':_('User with this email does not exist')},status=status.HTTP_404_NOT_FOUND)

#         try:
#             validate_password(password,user=user)
#         except ValidationError as error:
#             return Response({'error':error.message},status=status.HTTP_400_BAD_REQUEST)

#         user.set_password(password)
#         user.save()
#         return Response({'Success':_('Password has been reset successfully.')},status=status.HTTP_200_OK)


#Method Two for Password Reset
# from django.contrib.auth.models import User
# from django.core.mail import send_mail
# from django.utils.crypto import get_random_string
# from django.views import View
# from django.http import JsonResponse

# class ResetPasswordView(View):
#     def post(self, request, *args, **kwargs):
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'Email not found'}, status=404)

#         # Generate a random password
#         new_password = get_random_string(length=8)
#         user.set_password(new_password)
#         user.save()

#         # Send email with new password
#         subject = 'Password reset'
#         message = f'Your new password is: {new_password}'
#         send_mail(subject, message, 'admin@example.com', [email], fail_silently=False)

#         return JsonResponse({'message': 'Password reset successfully'})
















# class CheckRegistr(APIView):

#     permission_classes = [IsAuthenticated]
    

#     def get(self,request,format=None,*args,**kwargs):
#         indiviual = UserAccount.objects.get(user=request.user)
#         try:
#             indiviual = UserAccount.objects.get(user=request.user)
#             return Response('Man you registred')
#         except indiviual.DoesNotExist:
#             return Response('Register Please')


# # Complete student registration
# class StudentCreate(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request, format=None, *args, **kwargs):
#         student = StudentSerializer(data=request.data)
#         if student.is_valid():
#             student.save(user=request.user)
#             sendMail(request)
#             return Response(student.data, status=status.HTTP_201_CREATED)
#         return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class StudentList(APIView):
#     def get(self,request,format=None,*args,**kwargs):
#         student_profile = StudentProfile.objects.all()
#         serializer_class = StudentSerializer(student_profile)
        

#         return Response(serializer_class,status=status.HTTP_200_OK)
    
           


# class StudentCreate(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = StudentProfile.objects.all()
#     serializer_class = StudentSerializer
