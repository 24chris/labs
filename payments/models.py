from email.policy import default
from random import choices
from django.db import models
from django.conf import settings

from course.models import Course

class Invoice(models.Model):
    class State(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
        CANCELLED = "CANCELLED"

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True)
    date = models.DateField()
    due_date = models.DateField()
    state = models.CharField(max_length=15,choices=State.choices,default=State.UNPAID)

class ItemLine(models.Model):
    invoice = models.ForeignKey(to=Invoice,on_delete=models.PROTECT)
    quantity = models.IntegerField()
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    name_of_course = models.ForeignKey(Course,on_delete=models.PROTECT,null=True)


