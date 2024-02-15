from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import myDashboard
# Create your views here.
def hello(request):
    return HttpResponse("Hi am active")
def Ticket(request):
    dashboardData=myDashboard.objects.all()
    data={'dashboardData':dashboardData

    }
    return render(request,'index.html',data)
def aboutTicket(request):
    return render(request,'about_ticket.html',)