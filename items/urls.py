from django.urls import path

from items import views


urlpatterns = [
    path('item/<pk>/', views.ItemsView.as_view())
]