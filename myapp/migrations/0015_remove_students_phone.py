# Generated by Django 3.2.4 on 2021-06-17 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20210617_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='phone',
        ),
    ]