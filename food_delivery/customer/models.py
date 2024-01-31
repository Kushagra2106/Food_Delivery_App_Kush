#None
#    Of
#      A
#       Kind
from django.db import models

# Create your models here.

#make migrations=make changes and store
#migrate-apply the changes


class ThreeZeroOne(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
    
class ANC(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
    

class DCC(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
   
class FM(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
   
class PC(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
   
    
class Ltrs(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
    
    

class Tott(models.Model):
    name=models.CharField(max_length=121)

    def __str__(self):
        return self.name
    
    