from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from rest_framework import generics
from django.urls import reverse


from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import NonStudentSerializer
from .models import NonStudentProfile

from users.models import UserAccount


User = get_user_model()



# Send registered user mail
def sendMail(request):
    template = render_to_string('letter.html', {'name': request.user.username})
    email = EmailMessage(
        'Intern Letter',
        template,
        'ictlabs@example.com',
        ['mark@example.com'],
    )
    email.send()

    return Response({"Email sent successfully": "Some more"})


#Complete Non-student registration
class NonStudentCreate(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request,format=None, *args, **kwargs):
        non_student = NonStudentSerializer(data=request.data)
        if non_student.is_valid():
            non_student.save(user=request.user)
            sendMail(request)
            return Response(non_student.data, status=status.HTTP_201_CREATED)
        return Response(non_student.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def studentCreate(request):
#         student = StudentSerializer(data=request.data)
#         if student.is_valid():
#             student.save(user=request.user)
#             sendMail(request)
#             return Response(student)
#         return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)



