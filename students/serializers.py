from dataclasses import field
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import serializers
from users.models import UserAccount
from users.serializers import UserSerializer
from .models import StudentProfile

User = get_user_model()


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ('id', 'user', 'university', 'title_of', 'college', 'department', 'telephone', 'coursefield', 'specify_course', 'department_choice',
                  'year_of_study', 'registration_number', 'area_of_residence', 'guardian_name', 'guardian_number', 'work_type', 'start_time', 'end_time')
        # extra_kwargs = {
        #     'user_id':{'source':'user'}
        # }
        # Removed from serializer because of JSON
        # 'intern_picture','student_id_picture',
        # Add to fields when required

    def create(self, validated_data):
        profile = StudentProfile.objects.create(**validated_data)
        return profile