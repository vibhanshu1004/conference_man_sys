from django.urls import path
from .views import send_email, success

urlpatterns = [
    path('send-email/', send_email, name='send_email'),
    path('success/', success, name='success'),
]
