# Generated by Django 4.2.1 on 2023-06-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzashopapp', '0006_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bascet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.ImageField(upload_to='')),
            ],
        ),
    ]
