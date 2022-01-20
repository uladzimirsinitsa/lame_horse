from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:slug>', CasinoDetailView.as_view(), name='casino_detail_en'),
    path('<str:slug>/', slash_redirect_slug),
    path('', slash_redirect),
]