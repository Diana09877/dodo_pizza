# Generated by Django 5.1.3 on 2024-11-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(help_text='указывать в сомах')),
                ('volume', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(upload_to='drink_images')),
            ],
            options={
                'verbose_name': 'Напиток',
                'verbose_name_plural': 'Напитки',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField(help_text='указывать в сомах')),
                ('consist', models.TextField()),
                ('image', models.ImageField(upload_to='pizza_images')),
                ('size', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
            },
        ),
    ]
