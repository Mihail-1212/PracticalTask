# Generated by Django 3.0.6 on 2020-12-07 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название задачи')),
                ('text', models.TextField(blank=True, max_length=1024, verbose_name='Текст задачи')),
                ('date_start', models.DateTimeField(verbose_name='Запланированное время выполнения')),
                ('status', models.CharField(choices=[('Not_done', 'Unexecuted'), ('Done', 'Executed')], default='Not_done', max_length=50, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
