# Generated by Django 3.2.6 on 2021-08-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0008_auto_20210815_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='editor.Tag'),
        ),
    ]