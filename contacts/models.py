from django.db import models
from django.utils import timezone

"""
MODEL THAT WE ARE GOING TO IMPLEMENT HERE: 

CONTACTS
id: INT (automatic)
name: STR * (mandatory)
surname: STR (optional)
phone_number: STR * (mandatory)
email: STR (optional)
creation_date: DATETIME (automatic)
description: texto
category: CATEGORIA (outro model)

 CATEGORY
 id: INT
 name: STR * (mandatory)

"""
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True) #blank = True, because its optional 
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    creation_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING) 

    def __str__(self):
        return self.name


