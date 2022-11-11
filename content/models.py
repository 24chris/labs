from django.db import models

class Landing_Page_Information(models.Model):
    why_field = models.CharField(max_length=255)
    about_intern = models.CharField(max_length=255)
    about_supervision = models.CharField(max_length=255)
    about_skills = models.CharField(max_length=255)
    about_solutions = models.CharField(max_length=255)
    about_us = models.CharField(max_length=255)
    about_views = models.CharField(max_length=255)
    follow_us = models.CharField(max_length=255)
    contact_us = models.CharField(max_length=255)
    pricing = models.CharField(max_length=255)
    demo = models.CharField(max_length=255)
    partners = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('-demo',)

    def __str__(self):
        return self.about_us

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Introduction_Video(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
