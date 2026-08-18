from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class ConcertModel(models.Model):
    Name=models.CharField(max_length=100)
    singer_name=models.CharField(max_length=100)
    Price=models.FloatField()
    Time=models.IntegerField()
    poster=models.ImageField(upload_to="images/concert/",null=True)
    def __str__(self):
        return self.Name
class LocationModel(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=250)
    Phone=models.CharField(max_length=11,null=True)
    Capacity=models.IntegerField()
    def __str__(self):
        return self.Name
class TimeModel(models.Model):
    concert_model=models.ForeignKey(to=ConcertModel,on_delete=models.PROTECT)
    location_model=models.ForeignKey(to=LocationModel,on_delete=models.PROTECT)
    start_datetime=models.DateTimeField()
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
        return "Time:{}\nConcertName:{}\nLocation:{}".format(self.start_datetime,self.concert_model.Name,self.location_model.Name)
class UserModel(models.Model):
    Name= models.CharField(max_length=50)
    Family=models.CharField(max_length=50)

    profile=models.ImageField(upload_to="images/user/",null=True)
    phone_number = models.CharField(
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
class TicketModel(models.Model):
    time_model=models.ForeignKey(to=TimeModel,on_delete=models.PROTECT)
    user_model=models.ForeignKey(to=UserModel,on_delete=models.PROTECT)
    amount=models.IntegerField()
    ticket_image=models.ImageField(upload_to="images/ticket/",null=True)
    def total_price(self):
        return self.time_model.concert_model.Price*self.amount

    def __str__(self):
        return "Ticket info:\n{}\nCustomer:{}\nPrice:{}".format(self.time_model.__str__(),self.user_model.__str__(),self.total_price())
    