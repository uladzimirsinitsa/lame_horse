from django.urls import path
from .views import *


urlpatterns = [
    path('<str:slug>', NewsDetailView.as_view(), name='news_detail_en'),
    path('<str:slug>/', slash_redirect_slug),
    path('', slash_redirect),
]