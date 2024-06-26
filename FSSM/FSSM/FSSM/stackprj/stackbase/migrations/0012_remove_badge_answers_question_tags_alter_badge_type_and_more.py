# Generated by Django 5.0.6 on 2024-06-15 20:33

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0011_tag'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='answers',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='type',
            field=models.CharField(choices=[('question', 'Question Badge'), ('tag', 'Tag Badge')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
