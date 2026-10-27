from django import forms
from django.utils import timezone
from .models import Booking

class BookingForm(forms.ModelForm):
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control", "id": "reservation_date"}),
        initial=timezone.localdate,
    )
    reservation_slot = forms.TypedChoiceField(
        choices=[(hour, f"{hour}:00") for hour in range(10, 21)],
        coerce=int,
        widget=forms.Select(attrs={"class": "form-control", "id": "reservation_slot"}),
    )

    class Meta:
        model = Booking
        fields = ["name", "reservation_date", "reservation_slot"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"})}

    def clean(self):
        cleaned = super().clean()
        date = cleaned.get("reservation_date")
        slot = cleaned.get("reservation_slot")
        if date and date < timezone.localdate():
            self.add_error("reservation_date", "Choose today or a future date.")
        if date and slot is not None and Booking.objects.filter(reservation_date=date, reservation_slot=slot).exists():
            self.add_error("reservation_slot", "That time is already booked. Please choose another slot.")
        return cleaned
