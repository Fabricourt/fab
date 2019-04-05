from django.shortcuts import render,  redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import BookingForm
from .models import Booking
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from.models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking(request):
    template ="booking.html"

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
    else:
       
        form = BookingForm()

    bookings = Booking.objects.order_by('-booking_date').filter(is_published=True)
    context ={
        'bookings':bookings,
        'form': form,
    }


    messages.success(request, 'Your booking has been recieved')
    return render (request,  template, context)

  


  