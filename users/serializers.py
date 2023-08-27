from dataclasses import field
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import serializers
from users.models import UserAccount

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    #add confirm password field here then add it to the meta field and validate method can compare them and act appropriately

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "id",
            "role",
        ]


# class StudentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = StudentProfile
#         fields = ('id', 'user', 'university', 'title_of', 'college', 'department', 'telephone', 'coursefield', 'specify_course', 'department_choice',
#                   'year_of_study', 'registration_number', 'area_of_residence', 'guardian_name', 'guardian_number', 'work_type', 'start_time', 'end_time')
        

#     def create(self, validated_data):
#         profile = StudentProfile.objects.create(**validated_data)
#         return profile


# class UserCreateSerializer(UserCreateSerializer):   serializers.ModelSerializer
#     class Meta(UserCreateSerializer.Meta):
#         model = UserAccount
#         fields = ('id','email','name','password',)


# Test two - djoser stuff
# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = UserAccount
#         fields = ('username','email','password','role')


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserAccount
#         fields = ('id','username','email','password','role')
#         extra_kwargs = {'password':{'write_only':True}}


# And by the way I think you should create a serializer inheriting from djoser.serializers.UserSerializer and not from djoser.serializers.UserCreateSerializer for user and cuttent_user keys.


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )

#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
#         extra_kwargs = {
#             'first_name': {'required': True},
#             'last_name': {'required': True}
#         }

#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError({"password": "Password fields didn't match."})

#         return attrs

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )


#         user.set_password(validated_data['password'])
#         user.save()

#         return user
