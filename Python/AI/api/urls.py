from django.urls import path
from . import views

urlpatterns = [
    path('', views.sr71_view, name='SR'),
]