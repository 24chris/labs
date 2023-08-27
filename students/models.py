from django.db import models
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    university = models.CharField(max_length=20,blank=True)
    title_of = models.CharField(max_length=20,blank=True)
    college = models.CharField(max_length=20,blank=True)
    department = models.CharField(max_length=20,blank=True)
    telephone = models.CharField(max_length=20,blank=True)
    coursefield = models.CharField(max_length=20,blank=True)
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
        return f"{self.university} - {self.user}"

