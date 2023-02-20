from django.shortcuts import render
from django import views
from django.views import generic
from django.shortcuts import get_object_or_404
from django.conf import settings

from .models import Items


STRIPE_PUBLISH = settings.STRIPE_PUBLISH_KEY

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

class ItemsView(views.View):

    def get(self,request, pk):
        item = get_object_or_404(Items, pk=pk)
        context = {}
        context['id'] = item.pk
        context['name'] = item.name
        context['description'] = item.description
        context['price'] = item.price
        context['stripe_publish'] = STRIPE_PUBLISH
        return render(request, 'item_detail.html', context)


class ItemsList(generic.ListView):
    paginate_by = 2
    model = Items
    template_name = "item_list.html"
    context_object_name = "item_list"