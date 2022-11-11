from django.contrib import admin

from .models import UserAccount,Student,StudentProfile,NonStudent,NonStudentProfile

admin.site.register(UserAccount)
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(NonStudent)
admin.site.register(NonStudentProfile)
