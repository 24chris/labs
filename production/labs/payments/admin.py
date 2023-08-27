from django.contrib import admin

from .models import Invoice,ItemLine


admin.site.register(Invoice)
admin.site.register(ItemLine)