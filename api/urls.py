from django.urls import path
from django.urls import include
from django.conf import settings


from . import views

urlpatterns = [
    path('file', views.consume_file, name='consume_file')
]
