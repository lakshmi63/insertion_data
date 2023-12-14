from django.db import models

# Create your models here.
class Dept(models.Model):
    ename=models.CharField(max_length=100,primary_key=True)
    loc=models.CharField(max_length=100)
    sal=models.IntegerField()

    def __str__(self):
        return self.ename

class Emp(models.Model):
    ename=models.ForeignKey(Dept,on_delete=models.CASCADE)
    dname=models.CharField(max_length=100)
    joindate=models.DateField()

    def __str__(self):
        return self.dname

class Salgrade(models.Model):
    dname=models.ForeignKey(Emp,on_delete=models.CASCADE)
    grade=models.CharField(max_length=100)
    
    def __str__(self):
        return self.grade
