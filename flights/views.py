from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

import flights
from .models import Flight, Passenger
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html",{
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "nonPassengers" : Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.post["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(passenger)
        return HttpResponseRedirect(reverse("flights", args=(flight_id)))
    pass