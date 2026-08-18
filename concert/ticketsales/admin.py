from django.contrib import admin
from ticketsales.models import ConcertModel
from ticketsales.models import TicketModel
from ticketsales.models import TimeModel
from ticketsales.models import UserModel
from ticketsales.models import LocationModel

# Register your models here.
admin.site.register(TicketModel)
admin.site.register(TimeModel)
admin.site.register(UserModel)
admin.site.register(ConcertModel)
admin.site.register(LocationModel)
