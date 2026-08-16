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
    Phone=models.CharField(max_length=11,null=True)
    Capacity=models.IntegerField()
    def __str__(self):
        return self.Name
class timeModel(models.Model):
    concertModel=models.ForeignKey(to=concertModel,on_delete=models.PROTECT)
    locationModel=models.ForeignKey(to=locationModel,on_delete=models.PROTECT)
    startDateTime=models.DateTimeField()
    capacity=models.IntegerField()
