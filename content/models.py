from django.db import models

class Landing_Page_Information(models.Model):
    information_name = models.CharField(max_length=30)
    information_description = models.TextField(max_length=250,blank=True,null=True) 

    class Meta:
        ordering = ('-information_name',)

    def __str__(self):
        return self.information_name

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

class Information(models.Model):
    name=models.CharField(max_length=80)
    description = models.TextField(max_length=5000, blank=True,null=True)
    slug = models.SlugField()

    class Meta:
        ordering=('-name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'