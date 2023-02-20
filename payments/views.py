from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
import stripe
import re

from items.models import Items


stripe.api_key = settings.STRIPE_SECRET

@api_view(("GET", ))
def checkout_session(request: HttpRequest, item_id):
    item = Items.objects.get(pk=item_id)
    url = request.build_absolute_uri()
    pattern = "buy/\d+/"
    url = re.sub(pattern, '', url)
    print(url)
    session = stripe.checkout.Session.create(
        line_items=[
            {
            "price_data": {
                "currency": "usd",
                "product_data": {"name": item.name},
                "unit_amount": item.price,
            },
            "quantity": 1,
            },
        ],
        mode="payment",
        success_url=f'{url}success',
        cancel_url=f'{url}cancel',
    )
    return Response(session.to_dict())
    
