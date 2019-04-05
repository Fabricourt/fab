from django.shortcuts import render,  redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import TestamentForm
from .models import Testament
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

@login_required
def testament(request):
    template ="testament.html"

    if request.method == "POST":
        form = TestamentForm(request.POST)

        if form.is_valid():
            form.save()
    else:
       
        form = TestamentForm()
        

     
    
    testaments = Testament.objects.order_by('-post_date').filter(is_published=True)
    context ={
        'testaments':testaments,
        'form': form,
    }


    messages.success(request, 'Your testament has been recieved')
    return render (request,  template, context)

