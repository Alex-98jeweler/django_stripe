from django.urls import path

from items import views


urlpatterns = [
    path('item/<int:pk>/', views.ItemsView.as_view())
]