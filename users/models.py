from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class UserAccount(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT",'Student'
        NON_STUDENT = "NON-STUDENT",'Non-Student'

    role = models.CharField(max_length=50,choices=Role.choices)
    
    email = models.EmailField(max_length=40,unique=True)
    username = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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

@receiver(post_save,sender=Student)
def create_user_profile(sender,instance,created,**kwargs):
    if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True,blank=True)
    university = models.CharField(max_length=20,blank=True)
    title_of = models.CharField(max_length=20,blank=True)
    college = models.CharField(max_length=20,blank=True)
    department = models.CharField(max_length=20,blank=True)
    telephone = models.CharField(max_length=20,blank=True)
    coursefield = models.CharField(max_length=20,blank=True)
                # course = models.CharField(max_length=20)
    specify_course = models.CharField(max_length=20,blank=True)
    department_choice = models.CharField(max_length=20,blank=True)
    year_of_study = models.PositiveIntegerField(null=True,blank=True)
    registration_number = models.CharField(max_length=20,blank=True)
    area_of_residence = models.CharField(max_length=20,blank=True)
    guardian_name = models.CharField(max_length=20,blank=True)
    guardian_number = models.CharField(max_length=11,blank=True)
    intern_picture = models.ImageField(upload_to='uploads/', blank=True)
    student_id_picture = models.ImageField(upload_to='uploads/', blank=True)
    work_type = models.CharField(max_length=20,blank=True, )
    start_time = models.TimeField(blank=True, null = True)
    end_time = models.TimeField(blank=True,null=True)

    class Meta:
            ordering = ('-university',)

    def __str__(self):
        return self.university


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



class NonStudentProfile(models.Model):
    class Interest(models.TextChoices):
        BEGINNER = "BEGINNER",'Beginner'
        INTERMEDIATE = "INTERMEDIATE",'Intermediate'
        ADVANCED = "ADVANCED",'Advanced'

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    non_student_id = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=20,blank=True)
    program_of_interest = models.CharField(max_length=50,null=True,choices=Interest.choices)
    








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
