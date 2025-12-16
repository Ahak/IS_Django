from django.shortcuts import render, redirect
from .models import Drivers, Vehicles, Routes, Deliveries, bookings

# Create your views here.
def home(request):
    drivers = Drivers.objects.all()
    vehicles = Vehicles.objects.all()
    routes = Routes.objects.all()
    deliveries = Deliveries.objects.all()
    booking_list = bookings.objects.all()
    context = {
        'drivers': drivers,
        'vehicles': vehicles,
        'routes': routes,
        'deliveries': deliveries,
        'bookings': booking_list,
    }
    return render(request,'index.html', context)

def add_driver(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Drivers.objects.create(D_Name=name, D_EMail=email, D_Phone=phone)
    return redirect('home')

def add_vehicle(request):
    if request.method == 'POST':
        number = request.POST['number']
        v_type = request.POST['v_type']
        capacity = request.POST['capacity']
        driver_id = request.POST['driver']
        driver = Drivers.objects.get(id=driver_id)
        Vehicles.objects.create(V_Number=number, V_Type=v_type, V_Capacity=capacity, Driver=driver)
    return redirect('home')

def add_route(request):
    if request.method == 'POST':
        start = request.POST['start']
        end = request.POST['end']
        distance = request.POST['distance']
        vehicle_id = request.POST['vehicle']
        vehicle = Vehicles.objects.get(id=vehicle_id)
        Routes.objects.create(R_Start=start, R_End=end, R_Distance=distance, Vehicle=vehicle)
    return redirect('home')

def add_delivery(request):
    if request.method == 'POST':
        item = request.POST['item']
        weight = request.POST['weight']
        route_id = request.POST['route']
        date = request.POST['date']
        route = Routes.objects.get(id=route_id)
        Deliveries.objects.create(D_Item=item, D_Weight=weight, Route=route, Delivery_Date=date)
    return redirect('home')

def add_booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        pickup = request.POST['pickup']
        dropoff = request.POST['dropoff']
        pickup_date = request.POST['pickup_date']
        return_date = request.POST.get('return_date')
        vehicle_type = request.POST['vehicle_type']
        bookings.objects.create(
            name=name, email=email, phone=phone, pickup_location=pickup,
            dropoff_location=dropoff, pickup_date=pickup_date,
            return_date=return_date if return_date else None, vehicle_type=vehicle_type
        )
    return redirect('home')