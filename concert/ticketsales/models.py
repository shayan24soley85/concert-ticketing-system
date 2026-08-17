from django.db import models
from django.core.validators import MinLengthValidator
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
    started=1
    finished=2
    sale_open=3
    cancled=4
    status_choice=(("started","Ticket sales have started"),("finished","Tickets are sold out"),("sale_open","Tickets are available for sale"),("cancled","The concert has been canceled"))
    status=models.IntegerField(choices=status_choice)
    def __str__(self):
        return "Time:{}\nConcertName:{}\nLocation:{}".format(self.startDateTime,self.concertModel.Name,self.locationModel.Name)
class userModel(models.Model):
    Name= models.CharField(max_length=50)
    Family=models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('Male', 'مرد'),
        ('Female', 'زن'),
    )

    Name = models.CharField(max_length=100)
    Family = models.CharField(max_length=100)

    phoneNumber = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)], 
        null=True, 
        blank=True 
    )
    
    gender = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
    )
    