from django.urls import path, include
from . import views
from django.conf.urls import url
from .views import(
    TodoListApiView,
)



urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('api/', TodoListApiView.as_view()),
    ]