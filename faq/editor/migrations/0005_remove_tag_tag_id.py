# Generated by Django 3.2.6 on 2021-08-11 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_auto_20210810_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_id',
        ),
    ]
