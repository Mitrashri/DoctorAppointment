from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import appointments
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def appointment(request):
    return render(request,"appointment.html")

def patient(request):
    return render(request,"patientIndex.html")

def doctor(request):
    data = appointments.find()
    return render(request,"DoctorIndex.html",{"data":data})

def book_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "date": date,
            "time": time,
            "reason": reason
        }
        appointments.insert_one(data)
        return render(request,"success.html",{"message":"Appointment booked successfully!"})
    

def delete(request):
    print(request.GET)
    if "delete" in request.GET:
        appointments.delete_one({'phone':request.GET["phone"]})
    
    return render(request,"index.html")