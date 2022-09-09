from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def home_page(request):
    tasks_list = Task.odjects.all()
    context = {
        'task_list': tasks_list,
        'title': 'Главная страница',
    }

    return render(request, 'todo/index.html', context=context)


def show_category(request, cat_id):
    categories_list = Category.objects.all()
    context = {
        'categories_list': categories_list,
        'title': 'Страница категорий'

    }
    return render(request, 'todo/index.html', context=context)


def show_task(request, task_id):  # здесь должна присутствовать функция редактирования и удаления задачи
    task_list = Task.objects.get(pk=task_id)
    context = {
        'task_list': task_list,
        'title': 'Отображение задачи'
    }
    return render(request, '', context=context)


def create_task(request):
    pass


def login(request):
    pass


def signup(request):
    pass
