# Generated by Django 5.0.4 on 2024-05-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
