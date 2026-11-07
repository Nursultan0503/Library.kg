from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('verify/', views.verify_view, name='verify'),
    path('verify/resend/', views.resend_code_view, name='resend_code'),
    path('login/', views.auth_login_view, name='login'),
    path('logout/', views.auth_logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
