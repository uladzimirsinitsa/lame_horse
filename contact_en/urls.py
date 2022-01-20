from django.urls import path
from contact_en.views import contact_en

urlpatterns = [
    path('', contact_en, name="contact_form_en"),
]