from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
# Create your views here.

def index(request):
  return render(request, 'index.html')

def contact(request): 
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    contact = Contact()
    contact.name = name
    contact.email = email
    contact.subject = subject
    contact.message = message
    contact.save()
    return render (request, 'contact.html')
def base(request):
  return render(request, 'base.html')