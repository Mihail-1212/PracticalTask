from django.conf import settings
from django.db import models

class Task(models.Model):
    class AVAILABLE_STATUSES(models.TextChoices):
        not_done = 'Not_done', 'Не выполнено'
        done = 'Done', 'Выполнено'

    name = models.CharField(max_length=256, blank=False, verbose_name='Название задачи')
    text = models.TextField(max_length=1024, blank=True, null=True, verbose_name='Текст задачи')
    date_start = models.DateTimeField(verbose_name='Запланированное время выполнения')
    status = models.CharField(max_length=50, blank=False, choices=AVAILABLE_STATUSES.choices, default=AVAILABLE_STATUSES.not_done, verbose_name='Статус')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
