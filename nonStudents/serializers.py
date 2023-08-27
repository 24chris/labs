from dataclasses import field
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import serializers
from users.models import UserAccount
from users.serializers import UserSerializer
from .models import NonStudentProfile

User = get_user_model()


class NonStudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = NonStudentProfile
        fields = ('id', 'user', 'program_of_interest', 'level_of_skill','phone')
        # extra_kwargs = {
        #     'user_id':{'source':'user'}
        # }
        # Removed from serializer because of JSON
        # 'intern_picture','student_id_picture',
        # Add to fields when required

    def create(self, validated_data):
        non_profile = NonStudentProfile.objects.create(**validated_data)
        return non_profile