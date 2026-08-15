from django.db import models

# Create your models here.
class concertModel(models.Model):
    Name=models.CharField(max_length=100)
    SingerName=models.CharField(max_length=100)
    Price=models.FloatField()
    Time=models.IntegerField()
    def __str__(self):
        return self.Name
class locationModel(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=250)
    Phone=models.CharField(max_length=11)
    Capacity=models.IntegerField()
    def __str__(self):
        return self.Name
        