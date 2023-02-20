from django.urls import path

from payments import views


urlpatterns = [
    path("buy/<item_id>/", views.checkout_session, )
]