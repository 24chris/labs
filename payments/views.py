from logging import log
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

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
    
            
        
