# Generated by Django 5.0.6 on 2024-06-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0010_remove_question_tags_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
