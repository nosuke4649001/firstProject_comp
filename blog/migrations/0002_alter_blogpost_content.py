# Generated by Django 3.2.5 on 2021-09-09 19:25

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
    ]
