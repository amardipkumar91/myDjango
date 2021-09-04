# Generated by Django 3.2.4 on 2021-07-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_class', models.CharField(blank=True, max_length=50, null=True)),
                ('present', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student_class',
            },
        ),
        migrations.CreateModel(
            name='StudentClassnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_class', models.CharField(blank=True, max_length=50, null=True)),
                ('roll', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=30, null=True)),
                ('present2', models.IntegerField(blank=True, null=True)),
                ('present', models.IntegerField(blank=True, null=True)),
                ('present3', models.IntegerField(blank=True, null=True)),
                ('grade1', models.CharField(blank=True, max_length=30, null=True)),
                ('grade2', models.CharField(blank=True, max_length=30, null=True)),
                ('grade3', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'student_classnew',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('roll', models.IntegerField()),
                ('s_class', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'GG Students',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='myapp.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
