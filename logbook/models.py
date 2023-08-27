from PIL import Image
from io import BytesIO

from django.core.files import File
from django.db import models
from django.conf import settings
import uuid
from django.utils.text import slugify

class Logbook(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    week_number = models.CharField(max_length=40)
    task_completed = models.TextField(max_length=5000, blank=True,null=True)
    task_in_progress = models.TextField(max_length=5000, blank=True,null=True)
    next_day_task = models.TextField(max_length=5000, blank=True,null=True)
    problem_or_challenges = models.TextField(max_length=5000, blank=True,null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('week_number',)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.week_number)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.week_number

    def get_absolute_url(self):
        return f'/{self.slug}/'
