# Generated by Django 3.2.4 on 2021-06-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_studentclassnew_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclassnew',
            name='grade1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentclassnew',
            name='grade2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='studentclassnew',
            name='grade3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
