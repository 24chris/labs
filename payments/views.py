from logging import log
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import os
from rave_python import Rave,RaveExceptions, Misc

from .models import Invoice,Course
# from course.models import Enrolled
# from course.serializersOLD import EnrolledSerializer



# create payment modal 
class PaidCourse(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,course_slug,request,*args,**kwargs):
        course = Course.objects.get(slug=course_slug)
        is_paid = Invoice.objects.filter(name_of_course=course)
        
        if is_paid == Invoice.State.PAID:
            return Response("The course has been paid for!")
        else:
            return Response("The course has not been paid for!")
        return Response("A bunch of stuff going on!")



class PayForCourse(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
       return Response('You are attempting to pay for a course')
    
    


    # def get_object(self):
    #     return get_object_or_404(Course,slug=self.kwargs.get('slug'))
        
        
    # def get(self,request,*args,**kwargs):
    #     course = self.get_object(**kwargs)
    #     user = request.user
    #     is_paid = Invoice.objects.filter(user,name_of_course=course).first()
        
    #     if is_paid and is_paid.state == Invoice.State.PAID:
    #         Response(print("You have paid for this course")) 
    #     else:
    #         Response(print("You have not paid for this course yet"))
    #     return Response(print('Default end.....!'))
         

    # def get(self,request,*args,**kwargs):
    #     course_slug = kwargs.get('slug')
    #     course = Course.objects.get(slug=course_slug)
    #     is_paid = Invoice.objects.filter(name_of_course=course).exists
    #     data = {
    #         'slug':course_slug,
    #         'name':course.name,
    #         'is_paid':is_paid,
    #     }
    #     return Response(print(data))







# class Payment(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         user = request.user
#         if user.has_paid:
#             enroll = Enrolled.objects.filter(user=user)
#             serializer = EnrolledSerializer(enroll,many=True)
#             return Response(print('The courses returned'))
            
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
            


#Create Charge usig flutterwave,works fine
class PaymentView(APIView):
    # Charge Using Card
    # def post(self,request,*args,**kwargs):
    #     # rave = Rave(os.getenv("PUBLIC_KEY"), os.getenv("FLUTTERWAVE_SECRET_KEY"))
    #     rave = Rave("PUBLIC_KEY", "SECRET_KEY", usingEnv = False)
    #     payload = {
    #                     "card_number": '4556052704172643',
    #                     "cvv": '899',
    #                     "expiry_month": '01',
    #                     "expiry_year": '23',
    #                     "currency": 'NGN',
    #                     "amount": '7500',
    #                     "email": 'developers@flutterwavego.com',
    #                     "fullname": 'Flutterwave Developers',
    #                     "tx_ref": 'MC-3243e',
    #                     "redirect_url": 'https://your-awesome.app/payment-redirect',
    #                 }
    #     try:              
    #         response = rave.Card.charge(payload)
    #         print(response)
    #     except RaveExceptions.CardChargeError as e:
    #         print(e.err["errMsg"])
    #         print(e.err["flwRef"])
    def post(self,request,*args,**kwargs):
        rave = Rave("FLWPUBK_TEST-0aef47dba99a60c07a74333e93bec52e-X","FLWSECK_TEST-f10ff869fc20a5dce1d0e77c068b17bb-X",usingEnv=False)
        # Mobile Payload
        payload = {
            "amount":"500",
            "email":"vivjochris@gmail.com",
            "phonenumber":"0774033234",
            "redirect_url":"https://fieldsimplified.com/",
            "IP":"",
            "txtRef":"123456",
        }
        try:
            res = rave.UGMobile.charge(payload)
            # res = rave.UGMobile.verify(res["txtRef"])
            # res = rave.UGMobile.verify(res["123456"])
            return Response(print(res))

        except RaveExceptions.TransactionChargeError as e:
            print(e.err)
            print(e.err["flwRef"])

        except RaveExceptions.TransactionVerificationError as e:
            print(e.err["errMsg"])
            print(e.err["txtRef"])














# class PaymentView(APIView):
#     def post(self,request,format=None):
#         return Response(print("We retrieved the data"))



#Payment Webhook
# class PaymentWebhook():


# In a Django-like app:
# import os

@require_POST
@csrf_exempt
def webhook(request):
    secret_hash = "4333e93bec52e-X"
    signature = request.headers.get("verif-hash")
    if signature == None or (signature != secret_hash):
        # This request isn't from Flutterwave; discard
        return HttpResponse(status=401)
    payload = request.body
    # It's a good idea to log all received events.
    log(payload)
    print(payload)
    # Do something (that doesn't take too long) with the payload
    return HttpResponse(status=200)
    
            

#Airtel Payments
# import requests
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': '*/*'
# }

# r = requests.post('https://openapiuat.airtel.africa/auth/oauth2/token', headers = headers)

# print(r.json())
    

# #collections api
# import requests
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': '*/*',
#   'X-Country': 'UG',
#   'X-Currency': 'UGX',
#   'Authorization: Bearer  UCLcp1oeq44KPXr8X*******xCzki2w'
# }

# r = requests.post('https://openapiuat.airtel.africa/merchant/v1/payments/', headers = headers)

# print(r.json())

#Body Parameter
# {
#       "reference": "Testing transaction",
#       "subscriber": {
#         "country": "UG",
#         "currency": "UGX",
#         "msisdn": 9999999999
#       },
#       "transaction": {
#         "amount": 1000,
#         "country": "UG",
#         "currency": "UGX",
#         "id": "random-unique-id"
#       }
# }
    

#Example Response
# {
#       "data": {
#         "transaction": {
#           "id": "ASDJBEJB4KRN5",
#           "status": "SUCCESS"
#         }
#       },
#       "status": {
#         "code": "200",
#         "message": "SUCCESS",
#         "result_code": "ESB000010",
#         "response_code": "DP00800001006",
#         "success": true
#       }
# }
    

#Cashout, withdraw the amount from payee wallet and credit in payeer wallet
# import requests
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': '*/*',
#   'X-Country': 'UG',
#   'X-Currency': 'UGX',
#   'Authorization: Bearer  UCLcp1oeq44KPXr8X*******xCzki2w'
# }
          
# r = requests.post('https://openapiuat.airtel.africa/standard/v1/cashout/', headers = headers)
          
# print(r.json())
          
#Body parameter
# {
#   "subscriber": {
#     "msisdn": 702698414
#   },
#   "transaction": {
#       "amount": 12345,
#       "id": 12968801260
#   },
#     "additional_info": [
#         {
#             "key": "remark",
#             "value": "AIRTXXXXXX"
#         }
#       ],
#     "reference": 1234567
# }

#Example Response
# {
#   "data": {
#     "id": "TestId24",
#     "status": "SUCCESS"
#   },
#   "status": {
#     "code": "200",
#     "message": "SUCCESS",
#     "response_code": "DP01000001001",
#     "success": true
#   }
# }

#Application requires Oauth2