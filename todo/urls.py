from .views import todo_list, add_todo, delete_todo, mark_completed
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.todo_list,  name="todo_list"),
    path('addd/', views.add_todo,  name="add_todo"),
    path('complete/<int:todo_id>/', views.mark_completed,  name="mark_completed"),
    path('delete/<int:todo_id>/', views.delete_todo,  name="delete_todo"),
]
