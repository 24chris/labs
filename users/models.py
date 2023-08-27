from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
#third-party password-reset
from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 

class UserAccount(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT",'Student'
        NON_STUDENT = "NON-STUDENT",'Non-Student'

    role = models.CharField(max_length=50,choices=Role.choices)
    
    email = models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def has_paid(self):
        return 'PAID'


    def save(self,*args,**kwargs):
        if not self.pk:
            self.role = self.role
            return super().save(*args,**kwargs)


class StudentManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=UserAccount.Role.STUDENT)

class Student(UserAccount):
    base_role = UserAccount.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for students"

# @receiver(post_save,sender=Student)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created and instance.role == "STUDENT":
#         StudentProfile.objects.create(user=instance)



#Non-students
class NonStudentManager(BaseUserManager):
    def get_queryset(self,*args,**kwargs):
        results = super().get_queryset(*args,**kwargs)
        return results.filter(role=UserAccount.Role.NON_STUDENT)

class NonStudent(UserAccount):
    base_role = UserAccount.Role.NON_STUDENT

    non_student = NonStudentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for Non-students"


#Third-party password reset
# @receiver(reset_password_token_created)
# def password_reset_token_created(sender,instance,reset_password_token,*args,**kwargs):
#     email_plaintext_message = "{}?token".format(reverse('password_reset:reset-password-request'),reset_password_token.key)

#     send_mail(
#         #title:
#         "Password Reset for ({title})".format(title="Field Simplified"),
#         #message:
#         email_plaintext_message,
#         #from:
#         "nonreply@fieldsimplified.local",
#         #to:
#         [reset_password_token.user.email]
#     )

# Copy link which is in email, will be similar to /api/password_reset/?token=339e80fe05e5ca9fc74799213f81a093d1f
# Now copy that token which comes in email and and post token and password to /api/password_reset/confirm/ api url.
# {
#     "token":"3339e80fe05e5ca9fc74799213f81a093d1f",
#     "password":"Password@123"
# }
# In Response you will get –
# {
#     "status": "OK"
# }



























# class NonStudentProfile(models.Model):
#     class Interest(models.TextChoices):
#         BEGINNER = "BEGINNER",'Beginner'
#         INTERMEDIATE = "INTERMEDIATE",'Intermediate'
#         ADVANCED = "ADVANCED",'Advanced'

#     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     non_student_id = models.IntegerField(null=True,blank=True)
#     phone = models.CharField(max_length=20,blank=True)
#     program_of_interest = models.CharField(max_length=50,null=True,choices=Interest.choices)
    








#Multi- user setup 
# class UserAccount(AbstractUser):
#     class Role(models.TextChoices):
#         STUDENT = "STUDENT",'Student'
#         NON_STUDENT = "NON-STUDENT",'Non-Student'

#     # base_role = Role.STUDENT

#     role = models.CharField(max_length=50,choices=Role.choices)
#     email = models.EmailField(max_length=255,unique=True)
#     username = models.CharField(max_length=255)
    
    

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def save(self,*args,**kwargs):
#         if not self.pk:
#             self.role = self.role
#             return super().save(*args,**kwargs)


# class StudentManager(BaseUserManager):
#     def get_queryset(self,*args,**kwargs):
#         results = super().get_queryset(*args,**kwargs)
#         return results.filter(role=User.Role.STUDENT)

# class Student(UserAccount):
#     base_role = UserAccount.Role.STUDENT

#     student = StudentManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "only for students"

# @receiver(post_save,sender=Student)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created and instance.role == "STUDENT":
#         StudentProfile.objects.create(user=instance)


# class StudentProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     student_id = models.IntegerField(null=True,blank=True)



# #Non-students Manager
# class NonStudentManager(BaseUserManager):
#     def get_queryset(self,*args,**kwargs):
#         results = super().get_queryset(*args,**kwargs)
#         return results.filter(role=User.Role.NON_STUDENT)

# class NonStudent(UserAccount):
#     base_role = UserAccount.Role.NON_STUDENT

#     non_student = NonStudentManager()

#     class Meta:
#         proxy = True

#     def welcome(self):
#         return "only for Non-students"



# class NonStudentProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     non_student_id = models.IntegerField(null=True,blank=True)


# @receiver(post_save,sender=Student)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created and instance.role == "NON-STUDENT":
#         StudentProfile.objects.create(user=instance)
