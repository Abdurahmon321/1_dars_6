from django.urls import path
from .views import salom

urlpatterns = [
    path('', salom)
]
