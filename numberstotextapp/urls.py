from django.urls import path
from .views import num_to_english

urlpatterns  = [
    path('num_to_english', num_to_english),
]