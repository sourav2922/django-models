from django.db import models

# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.FloatField(max_length=100)
    w_hrs=models.FloatField(max_length=50)
    ids=models.IntegerField(max_length=10)

    def __str__(self):
        return self.name
    

   
   


