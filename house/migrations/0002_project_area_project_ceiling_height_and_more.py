# Generated by Django 4.1.7 on 2023-04-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='area',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='ceiling_height',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='dimensions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='floors',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='height',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='roof',
            field=models.TextField(blank=True),
        ),
    ]
