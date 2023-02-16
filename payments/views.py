from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

import stripe

stripe.api_key = settings.STRIPE_SECRET

@api_view(("GET", ))
def checkout_session(request,):
    session = stripe.checkout.Session.create(
        line_items=[
            {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "T-shirt"},
                "unit_amount": 2000,
            },
            "quantity": 1,
            },
        ],
        mode="payment",
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return Response({'session_id': session.url})
    
