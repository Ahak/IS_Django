from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Drivers)
admin.site.register(Vehicles)
admin.site.register(Routes)
admin.site.register(Deliveries)
admin.site.register(bookings)