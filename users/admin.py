from django.contrib import admin

from .models import UserAccount,Student,NonStudent

admin.site.register(UserAccount)
admin.site.register(Student)
admin.site.register(NonStudent)

