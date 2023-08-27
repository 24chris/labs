from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings
import uuid
from django.utils.text import slugify


#category of the course
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='children')

#     def __str__(self):
#         return self.name
    
# #level of course
# class Level(models.Model):
#     name = models.CharField(max_length=200)
#     parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='children')


#Relate those models up to the course, i.e categories is a many to manyfield..


class Course(models.Model):
    class CourseType(models.TextChoices):
        STUDENT = "STUDENT",'Student'
        NON_STUDENT = "NON-STUDENT",'Non-Student'

    class CourseLevel(models.TextChoices):
        BEGINNER = "BEGINNER",'Beginner'
        INTERMEDIATE = "INTERMEDIATE",'Intermediate'
        ADVANCED = "ADVANCED",'Advanced'

    course_author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course_category = models.CharField(max_length=20,choices=CourseType.choices)
    course_level = models.CharField(max_length=30,choices=CourseLevel.choices)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=7 ,decimal_places=2)
    course_uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_module")
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=5000, blank=True,null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    module_uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('name',)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.course.slug}/{self.slug}/'

class Lesson(models.Model):
    course = models.ForeignKey(Course,related_name='course_lesson',on_delete=models.CASCADE)
    module = models.ForeignKey(Module,related_name='module_lesson',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=5000, blank=True,null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    lesson_uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    order = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('module','order')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.course.slug}/{self.module.slug}/{self.slug}/'




# class Enrolled(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrolled_user")
#     # course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolled_course")
#     paid = models.BooleanField(default=False)
#     enrollment_uuid = models.UUIDField(default=uuid.uuid4,unique=True)
#     date_enrolled = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('date_enrolled',)
#         # unique_together = ('user','course',)

#     def __str__(self):
#         return f"User: {self.user}, course: {self.paid}"


# class Registered(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     course = models.ForeignKey(Category, on_delete=models.CASCADE)
#     date_enrolled = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"User: {self.user}, course: {self.course}"


class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Lesson = models.ForeignKey(Lesson,default=True,on_delete=models.CASCADE,related_name='comments')
    message=models.TextField()
    comment_uuid = models.UUIDField(default=uuid.uuid4,unique=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User:- {self.user}, message:- {self.message}"

    def get_absolute_url(self):
        return f'/{self.Lesson}/{self.comment_uuid}/'






















