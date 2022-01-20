from django.urls import path
from .views import *


urlpatterns = [
    path('<str:slug>', PromoDetailView.as_view(), name='promo_detail_en'),
    path('<str:slug>/', slash_redirect_slug),
    path('', slash_redirect),
]