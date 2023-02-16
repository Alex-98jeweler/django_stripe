from django.shortcuts import render
from django import views

from .models import Items




class ItemsView(views.View):

    def get(request, pk):
        item = Items.objects.get(pk=pk)
        context = {}
        context['name'] = item.name
        context['description'] = item.description
        context['price'] = item.price
        return render(request, 'item_detail.html', context)
