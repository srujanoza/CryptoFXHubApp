from django.urls import path
from .views import signup_view, success_page_view

urlpatterns = [
    # Other URL patterns
    path('sign-up/', signup_view, name='signup'),
    path('success/', success_page_view, name='success_page'),
]
