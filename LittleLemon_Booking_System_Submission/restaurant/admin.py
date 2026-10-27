from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "reservation_date", "reservation_slot")
    list_filter = ("reservation_date", "reservation_slot")
    search_fields = ("name",)
