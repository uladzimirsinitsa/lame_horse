from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', lambda request: redirect('login_en', permanent=True)),
    path('login', MyLoginView.as_view(), name='login_en'),
    path('logout', LogoutViewEn.as_view(), name='logout_en'),
    path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change_en'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done_en'),
    path('password_reset/done', PasswordResetDoneEn.as_view(), name='password_reset_done_en'),
    path('password_reset', ResetViewEn.as_view(), name='password_reset_en'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm_en'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete_en'),
    path('register', register_en, name='register_en'),
    path('edit', edit_en, name='edit_en'),
]