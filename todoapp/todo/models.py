from django.db import models
from django.urls import reverse


class User(models.Model):  # первичная модель по отношению к модели Task
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    time_signup = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,
                            db_index=True)  # вторичная модель по отношению к модели Category
    user = models.ForeignKey('Task', on_delete=models.CASCADE,
                             db_index=True)  # вторичная модель по отношению к модели User

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_id': self.pk})


class Category(models.Model):  # первичная модель по отношению к модели Task
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
