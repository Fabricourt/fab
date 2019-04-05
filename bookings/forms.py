from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'user_id', 
            'first_name',
            'last_name',
            'ministry_name',
            'ministry_location',
            'county',
            'email',
            'address',
            'phone_number',
            'ministry_location',
            'description',
            'booking_date',
            'return_date',
            )
    
    def clean(self):
        form_booking_date = self.cleaned_data.get('booking_date')
        form_return_date = self.cleaned_data.get('return_date')
        between = Booking.objects.filter(booking_date__gte=form_booking_date, return_date__lte=form_return_date).exists()
        if between:
            raise forms.ValidationError("Period already between this date 1")
        super(BookingForm, self).clean()