from tkinter.tix import MAX
from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models

class Employee(models.Model):
    Name=models.CharField
    Email=models.EmailField
    mobile=models.IntegerField
    department=models.CharField
    collage=models.CharField
    salary=models.IntegerField

    

   
