from django.shortcuts import render
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

from .serializers import LogBookSerializer
from .models import Logbook

from users.models import UserAccount

User = get_user_model()

# Create an instance of the Logbook
class LogBookCreate(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request,format=None, *args, **kwargs):
        logbook = LogBookSerializer(data=request.data)
        if logbook.is_valid():
            logbook.save(user=request.user)
                        
            return Response(logbook.data, status=status.HTTP_201_CREATED)
        return Response(logbook.errors, status=status.HTTP_400_BAD_REQUEST)

