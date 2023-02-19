from django.shortcuts import render
from django import views
from django.views import generic

from .models import Items


def index(request):
    return render(request, 'index.html')


class ItemsView(views.View):

    def get(self,request, pk):
        item = Items.objects.get(pk=pk)
        context = {}
        context['id'] = item.pk
        context['name'] = item.name
        context['description'] = item.description
        context['price'] = item.price
        return render(request, 'item_detail.html', context)


class ItemsList(generic.ListView):
    paginate_by = 2
    model = Items
    template_name = "item_list.html"
    context_object_name = "item_list"