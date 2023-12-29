from django.urls import path
from .views import num_to_english


urlpatterns = [
    path('num_to_english', view=num_to_english, name="num_to_english"),
]