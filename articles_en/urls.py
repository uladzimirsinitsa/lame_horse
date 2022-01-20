from django.urls import path
from .views import *


urlpatterns = [
    path('<str:slug>', ArticleDetailView.as_view(), name='article_detail_en'),
    path('<str:slug>/', slash_redirect_slug),
    path('', slash_redirect),
]
