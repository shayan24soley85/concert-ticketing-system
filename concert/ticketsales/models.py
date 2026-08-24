from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class ConcertModel(models.Model):
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت‌ها"

    Name = models.CharField(max_length=100, verbose_name="نام کنسرت")
    singer_name = models.CharField(max_length=100, verbose_name="نام خواننده")
    Price = models.FloatField(verbose_name="قیمت پایه")
    Time = models.IntegerField(verbose_name="مدت زمان (دقیقه)")
    poster = models.ImageField(
        upload_to="images/concert/", null=True, blank=True, verbose_name="پوستر کنسرت"
    )

    def __str__(self):
        return self.Name


class LocationModel(models.Model):
    class Meta:
        verbose_name = "لوکیشن"
        verbose_name_plural = "لوکیشن‌ها"

    Name = models.CharField(max_length=100, verbose_name="نام سالن/مکان")
    Address = models.CharField(max_length=250, verbose_name="آدرس")
    Phone = models.CharField(max_length=11, null=True, verbose_name="شماره تماس")
    Capacity = models.IntegerField(verbose_name="ظرفیت کل")

    def __str__(self):
        return self.Name


class TimeModel(models.Model):
    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس‌ها"

    concert_model = models.ForeignKey(
        to=ConcertModel, on_delete=models.PROTECT, verbose_name="کنسرت"
    )
    location_model = models.ForeignKey(
        to=LocationModel, on_delete=models.PROTECT, verbose_name="سالن برگزاری"
    )
    start_datetime = models.DateTimeField(verbose_name="تاریخ و ساعت شروع")
    capacity = models.IntegerField(verbose_name="ظرفیت سانس")

    started = 1
    finished = 2
    sale_open = 3
    cancled = 4

    status_choice = (
        (started, "شروع فروش بلیط"),
        (finished, "تکمیل ظرفیت (تمام شده)"),
        (sale_open, "در حال فروش (موجود)"),
        (cancled, "کنسرت لغو شده"),
    )

    status = models.IntegerField(choices=status_choice, verbose_name="وضعیت فروش")

    def __str__(self):
        return "Time:{}\nConcertName:{}\nLocation:{}".format(
            self.start_datetime, self.concert_model.Name, self.location_model.Name
        )


class UserModel(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    Name = models.CharField(max_length=50, verbose_name="نام")
    Family = models.CharField(max_length=50, verbose_name="نام خانوادگی")

    profile = models.ImageField(
        upload_to="images/user/", null=True, verbose_name="عکس پروفایل"
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)],
        null=True,
        blank=True,
        verbose_name="شماره موبایل",
    )
    GENDER_CHOICES = (
        ("Male", "مرد"),
        ("Female", "زن"),
    )

    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, verbose_name="جنسیت"
    )

    def __str__(self):
        return "{} {}".format(self.Name, self.Family)


class TicketModel(models.Model):
    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط‌ها"

    time_model = models.ForeignKey(
        to=TimeModel, on_delete=models.PROTECT, verbose_name="سانس مربوطه"
    )
    user_model = models.ForeignKey(
        to=UserModel, on_delete=models.PROTECT, verbose_name="خریدار (کاربر)"
    )
    amount = models.IntegerField(verbose_name="تعداد بلیط")
    ticket_image = models.ImageField(
        upload_to="images/ticket/", null=True, verbose_name="تصویر بلیط"
    )

    def total_price(self):
        return self.time_model.concert_model.Price * self.amount

    def __str__(self):
        return "Ticket info:\n{}\nCustomer:{}\nPrice:{}".format(
            self.time_model.__str__(), self.user_model.__str__(), self.total_price()
        )
