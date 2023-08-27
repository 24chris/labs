from django.db import models
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings


class NonStudentProfile(models.Model):
    class Interest(models.TextChoices):
        BEGINNER = "BEGINNER",'Beginner'
        INTERMEDIATE = "INTERMEDIATE",'Intermediate'
        ADVANCED = "ADVANCED",'Advanced'

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    program_of_interest = models.CharField(max_length=30)    
    level_of_skill = models.CharField(max_length=50,null=True,choices=Interest.choices)
    phone = models.CharField(max_length=20,blank=True)
    
    class Meta:
            ordering = ('-program_of_interest',)

    def __str__(self):
        return f"{self.program_of_interest} - {self.user}"

    