# Generated by Django 4.2.1 on 2023-06-07 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_constractor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='max_point',
        ),
    ]
