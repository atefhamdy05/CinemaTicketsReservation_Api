from django.contrib import admin
from .models import Guest,Movie,Reservation
admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Movie)
# Register your models here.
