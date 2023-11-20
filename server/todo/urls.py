from .views import *
from django.urls import path


urlpatterns = [
    path('', listTodo.as_view()),
    path('create/', createTodo.as_view()),
    path('update/<int:pk>/', updateTodo.as_view()),
    path('delete/<int:pk>/', deleteTodo.as_view()),
]