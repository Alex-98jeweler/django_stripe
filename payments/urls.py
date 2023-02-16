from django.urls import path

from payments import views


urlpatterns = [
    path("buy/", views.checkout_session, )
]