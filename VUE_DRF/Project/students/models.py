from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=200)
    branch_name = models.CharField(max_length=200)
    section = models.CharField(max_length=1)

    def __str__(self):

        return f"{self.name} {self.branch_name} {self.section}"

    class Meta:

        ordering = ['name']
