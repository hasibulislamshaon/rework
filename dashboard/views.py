from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import myDashboard
# Create your views here.

def hello(request):
    return HttpResponse("Hi am active")

def Ticket(request):
    dashboardData=myDashboard.objects.all()
    context={'dashboardData':dashboardData}
    
    return render(request,'index.html',context)

def aboutTicket(request,slug,id):
    
    details=myDashboard.objects.get(id=id)

    #details=get_object_or_404(myDashboard,pk=id)
    context={"details":details}

    return render(request,'about_ticket.html',context)