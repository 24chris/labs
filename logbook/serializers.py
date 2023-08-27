from dataclasses import field, fields

from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from django.contrib.auth import get_user_model

from rest_framework import serializers
from users.models import UserAccount

from .models import Logbook
from users.serializers import UserSerializer

User = get_user_model()

class LogBookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Logbook
        fields = ('id','user','week_number','task_completed','task_in_progress','next_day_task','problem_or_challenges','slug','created_at','updated_at')

        def create(self, validated_data):
            logbook = LogBookSerializer.objects.create(**validated_data)
            return logbook

