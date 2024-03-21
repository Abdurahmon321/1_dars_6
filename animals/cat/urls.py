from django.urls import path
from . import views

urlpatterns = [
    path('', views.oyna_1, name='index.html'),
    path('oyna2/', views.oyna_2),
    path('oyna3/', views.oyna_3),
    path('oyna4', views.oyna_4),
    path('oyna5/', views.oyna_5)
]
