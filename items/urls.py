from django.urls import path

import views


urlpatterns = [
    path('item/<pk>/', views.ItemsView.as_view())
]