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
    started = 1
    finished = 2
    sale_open = 3
    cancled = 4
    
    
    status_choice = (
        (started, "Ticket sales have started"),
        (finished, "Tickets are sold out"),
        (sale_open, "Tickets are available for sale"),
        (cancled, "The concert has been canceled")
    )
    
    status = models.IntegerField(choices=status_choice)
    def __str__(self):
        return "Time:{}\nConcertName:{}\nLocation:{}".format(self.startDateTime,self.concertModel.Name,self.locationModel.Name)
class userModel(models.Model):
    Name= models.CharField(max_length=50)
    Family=models.CharField(max_length=50)

    
    phoneNumber = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)], 
        null=True, 
        blank=True 
    )
    GENDER_CHOICES = (
        ('Male', 'مرد'),
        ('Female', 'زن'),
    )
    
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES, 
    )
    def __str__(self):
        return "{} {}".format(self.Name,self.Family)
class ticketModel(models.Model):
    timeModel=models.ForeignKey(to=timeModel,on_delete=models.PROTECT)
    userModel=models.ForeignKey(to=userModel,on_delete=models.PROTECT)
    amount=models.IntegerField()
    def totalPrice(self):
        return self.timeModel.concertModel.Price*self.amount

    def __str__(self):
        return "Ticket info:\n{}\nCustomer:{}\nPrice:{}".format(self.timeModel.__str__(),self.userModel.__str__(),self.totalPrice())
    