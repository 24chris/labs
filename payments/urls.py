import imp
from django.urls import path, include
from .views import webhook,PaymentView,PaidCourse,PayForCourse

from payments import views

urlpatterns = [
    path('webhooks/flutterwave/',views.webhook,name='webhook'),
    path('create/new/payment/modal-creation/',views.PaymentView.as_view(),name='modal'),
    # path('paysort',views.Payment.as_view(),name='paysort'),

    # test modal creation
    path('<slug:course_slug>/paid-course/',views.PaidCourse.as_view(),name='paid-course'),

    #New Section
    path('course/pay/amount/chosen/pay-for-course/',views.PayForCourse.as_view(), name='payment'),

    
]