from django.db import models

# Create your models here.



class Company(models.Model):
  name = models.CharField(max_length=200, primary_key=True)
  bio = models.TextField(max_length=250, null=True, blank=True)
  
  def __str__(self):
    return self.name


class Advocates(models.Model):
  company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
  username = models.CharField(max_length=200, primary_key=True)
  bio = models.TextField(max_length=250, null=True, blank=True)
  
  def __str__(self):
    return self.username