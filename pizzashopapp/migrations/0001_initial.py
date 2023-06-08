# Generated by Django 4.2.1 on 2023-05-19 12:41

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
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('consist_of', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='pizzashopapp_pthoto_ather/')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('consist_of', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='pizzashopapp_photo_pizza/')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Soup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('consist_of', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='pizzashopapp_photo_soup/')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('consist_of', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('photo', models.ImageField(upload_to='pizzashopapp_photo_water/')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('option1', 'smol'), ('option2', 'normal'), ('option3', 'big')], max_length=20)),
                ('pizza', models.ManyToManyField(related_name='size', through='pizzashopapp.PizzaSize', to='pizzashopapp.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizzasize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzashopapp.size'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(auto_created=True, decimal_places=2, max_digits=10)),
                ('order_number', models.CharField(max_length=20)),
                ('order_description', models.TextField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='pizzasize',
            unique_together={('pizza', 'size')},
        ),
    ]
