from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["reservation_date", "reservation_slot"]
        constraints = [
            models.UniqueConstraint(
                fields=["reservation_date", "reservation_slot"],
                name="unique_booking_date_slot",
            )
        ]

    def clean(self):
        if self.reservation_date and self.reservation_date < timezone.localdate():
            raise ValidationError({"reservation_date": "Choose today or a future date."})
        if self.reservation_slot < 10 or self.reservation_slot > 20:
            raise ValidationError({"reservation_slot": "Choose a valid reservation time."})

    def __str__(self):
        return f"{self.name} — {self.reservation_date} at {self.reservation_slot}:00"
