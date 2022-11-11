from django.contrib import admin


from .models import Course,Module,Lesson

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.index_title = "FieldSimplified"
admin.site.site_header = "FieldSimplified"