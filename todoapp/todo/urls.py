
from django.contrib import admin
from django.urls import path
from todo.views import *

urlpatterns = [
    path('', home_page, name='task_list'),
    path('task/<int:task_id>', show_task, name='task'),
    path('category/<int:cat_id>', show_category, name='category')

]
