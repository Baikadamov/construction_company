# Generated by Django 4.1.7 on 2023-03-08 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Типы книг',
                'verbose_name_plural': 'Список типов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='house.type')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты компании',
                'ordering': ['name'],
            },
        ),
    ]