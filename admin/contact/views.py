from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        contact = Contact()
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact.fname = fname
        contact.lname = lname
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        return redirect('/')
    return render(request,'contactus.html')