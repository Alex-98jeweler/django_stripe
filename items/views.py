from django.shortcuts import render
from django import views

from .models import Items




class ItemsView(views.View):

    def get(self,request, pk):
        item = Items.objects.get(pk=pk)
        context = {}
        context['id'] = item.pk
        context['name'] = item.name
        context['description'] = item.description
        context['price'] = item.price
        return render(request, 'item_detail.html', context)
