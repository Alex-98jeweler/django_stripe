from django.urls import path

from items import views


urlpatterns = [
    path('items/', views.ItemsList.as_view(),),
    path('items/<int:pk>/', views.ItemsView.as_view()),
]