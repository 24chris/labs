from .serializers import UserCreateSerializer
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from rest_framework.response import Response
from django.template.loader import render_to_string

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer

from users.models import UserAccount



User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer



#Send registered user mail
def sendMail(request):
    template = render_to_string('letter.html',{'name':request.user})
    email = EmailMessage(
        'Intern Letter',
        template,
        'ictlabs@example.com',
        ['mark@example.com'],
    )
    email.send()

    return Response({"Email sent successfully":"Some more"})

    
    
# Complete student registration
class StudentCreate(APIView):
   
    def post(self,request,format=None):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            sendMail()
            return Response(student.data,status=status.HTTP_201_CREATED)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

