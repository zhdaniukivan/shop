# Generated by Django 4.2.1 on 2023-06-04 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0005_alter_pizza_photo_alter_soup_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('feedback', models.TextField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
    ]