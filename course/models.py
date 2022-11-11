# from tabnanny import verbose
# # from unicodedata import category
# from uuid import uuid3, uuid4
# from django.db import models

# class Course(models.Model):
#     name = models.CharField(max_length=30)
#     level = models.CharField(max_length=30)
#     slug = models.SlugField()

#     class Meta:
#         ordering = ('name',)
#         verbose_name_plural = "Courses"

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f'/{self.slug}/'

# # class Lesson(models.Model):
# #     course = models.ForeignKey(Course,related_name='Courses',on_delete=models.CASCADE,default=False)
# #     name = models.CharField(max_length=30)
# #     slug = models.SlugField()
# #     description = models.TextField(max_length=225)
# #     instructed_by = models.CharField(max_length=30)
# #     video_url = models.URLField(max_length=500)

# #     class Meta:
# #         ordering = ('name',)
# #         verbose_name_plural = "Lessons"

# #     def __str__(self):
# #         return self.name
    
# #     def get_absolute_url(self):
# #         return f'/{self.course}/{self.slug}/'



# # class Category(models.Model):
# #     name = models.CharField(max_length=30)
# #     slug = models.SlugField()

# #     class Meta:
# #         ordering = ('name',)
# #         verbose_name_plural = "Categories"

# #     def __str__(self):
# #         return self.name

# #     def get_absolute_url(self):
# #         return f'/{self.slug}/'


# # class Course(models.Model):
# #     category = models.ForeignKey(Category,related_name='Courses',on_delete=models.CASCADE,default=False)
# #     course_id = models.IntegerField(primary_key=True,default=True)
# #     name = models.CharField(max_length=50)
# #     slug = models.SlugField()
# #     description = models.CharField(max_length=50)
# #     instructed_by = models.CharField(max_length=50)
    

# #     class Meta:
# #         ordering = ('name',)
# #         verbose_name_plural = "Courses"

# #     def __str__(self):
# #         return self.name
    
# #     def get_absolute_url(self):
# #         return f'/{self.category}/{self.slug}/'



# # class Lesson(models.Model):
# #     course = models.ForeignKey(Course,related_name='lessons', on_delete=models.CASCADE)
# #     category = models.ForeignKey(Category,on_delete=models.CASCADE,default=False)
# #     lesson_id = models.UUIDField(primary_key=True,default=uuid4)
# #     name = models.CharField(max_length=50)
# #     instruments = models.CharField(max_length=50)
# #     # length = models.CharField(max_length=40)
# #     video_url = models.URLField(max_length=500)
# #     slug = models.SlugField()

# #     class Meta:
# #         ordering = ('name',)
# #         verbose_name_plural = "lessons"

# #     def __str__(self):
# #         return self.name

# #     def get_absolute_url(self):
# #         return f'/{self.slug}/{self}/{self.category}/{self.course}'



# Test feature

# from distutils.command.upload import upload
# from email.mime import image
# from unicodedata import category, name

from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings


class Course(models.Model):
    class CourseType(models.TextChoices):
        STUDENT = "STUDENT",'Student'
        NON_STUDENT = "NON-STUDENT",'Non-Student'

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=5000, blank=True,null=True)
    level = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    course_group = models.CharField(max_length=20,choices=CourseType.choices,null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Module(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_module")
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=5000, blank=True,null=True)
    level = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.course.slug}/{self.slug}/'

class Lesson(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,related_name='course_lesson',on_delete=models.CASCADE)
    module = models.ForeignKey(Module,related_name='module_lesson',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(max_length=5000, blank=True,null=True)
    level = models.CharField(max_length=30)
    video_url = models.CharField(max_length=500, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.course.slug}/{self.module.slug}/{self.slug}/'




class Enrolled(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrolled_user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrolled_course")
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user}, course: {self.course}"


# class Registered(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     course = models.ForeignKey(Category, on_delete=models.CASCADE)
#     date_enrolled = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"User: {self.user}, course: {self.course}"


# class Comment(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     message=models.TextField()
#     created=models.DateTimeField(auto_now=True)






















