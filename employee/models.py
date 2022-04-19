from unicodedata import name
from django.db import models
from django.forms import CharField
from sqlalchemy import ForeignKey

# Create your models here.
class role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "role"


class education(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "education"


class employee(models.Model):
    name = models.CharField(max_length=100)
    sirname = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    education = models.ForeignKey(education, on_delete=models.CASCADE)
    hiring_date = models.DateField()

    def __str__(self):
        return "%s %s" %(self.name, self.sirname)
    
    class Meta:
        verbose_name_plural = "employee"