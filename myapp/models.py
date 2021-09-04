from django.db import models
from phone_field import PhoneField

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    roll = models.IntegerField()
    # phone = PhoneField(blank=True, help_text='Contact phone number')
    s_class = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'GG Students'
        
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        name = self.name
        roll = self.roll
        age = self.age
        s_class = 'Name of Student: {0} and Roll is : {1}'.format(name, roll)
        self.s_class = s_class
        super(Students, self).save(*args, **kwargs)
        print ("Done")


        
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StudentClass(models.Model):
    s_class = models.CharField(max_length=50, blank=True, null=True)
    present = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'student_class'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class StudentClassnew(models.Model):
    s_class = models.CharField(max_length=50, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    grade = models.CharField(max_length=30, blank=True, null=True)
    present2 = models.IntegerField(blank=True, null=True)
    present = models.IntegerField(blank=True, null=True)
    present3 = models.IntegerField(blank=True, null=True)
    grade1 = models.CharField(max_length=30, blank=True, null=True)
    grade2 = models.CharField(max_length=30, blank=True, null=True)
    grade3 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'student_classnew'


class Publication(models.Model):
    title = models.CharField(max_length=30)
    class Meta:
        ordering = ['title']
    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline