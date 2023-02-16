from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe

from items.models import Items


stripe.api_key = settings.STRIPE_SECRET

@api_view(("GET", ))
def checkout_session(request, item_id):
    item = Items.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
        line_items=[
            {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "T-shirt"},
                "unit_amount": 50,
            },
            "quantity": 1,
            },
        ],
        mode="payment",
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return Response({'session_id': session.url})
    
