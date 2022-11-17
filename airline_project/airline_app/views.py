from django.shortcuts import render,redirect
from .  models import *
from django.contrib import messages
# Create your views here.
def base_page(request):
    return render(request,'base.html')

def home_page(request):
    return render(request,'home.html')

def about_page(request):
    return render(request,'about_us.html')

def contact_page(request):
    return render(request,'contact_us.html')

def login(request):
    return render(request,'login_latest.html')

def customer_home_page(request):
    return render(request,'customer_home_page.html')

def admin_home_page(request):
    return render(request,'admin_home_page.html')

def airlines_home_page(request):
    return render(request,'airlines_home_page.html')

def change_password_page(request):
    return render(request,'change_password.html')

def registration_customer_page(request):
    message=""
    if request.method == 'POST':
        customer_details = Customer()
        if Customer.objects.filter(username=request.POST['Username']).exists():
            # messages.info(request,'Username is already taken')
            message="Username is already taken"
        elif Customer.objects.filter(email=request.POST['Email']).exists():
            # messages.info(request,'Email already taken')
            message="Email is already taken"
        else:
            customer_details.fullname = request.POST['Fullname']
            customer_details.username = request.POST['Username']
            customer_details.email = request.POST['Email']
            customer_details.contact = request.POST['Contact']
            customer_details.password = request.POST['Password']
            customer_details.city = request.POST['City']
            customer_details.date_of_birth = request.POST['Date']
            customer_details.gender = request.POST['Gender']
            
            
            if len(request.FILES) != 0:
                customer_details.image = request.FILES['image'] 
            
            customer_details.save()
            message="Data inserted successfully"
            return render(request,'registration_customer.html',{'msg':message})
            
            
    return render(request,'registration_customer.html',{'msg':message})



def registration_airlines_page(request):
    message=""
    if request.method == 'POST':
        request_details = Request()
        if Request.objects.filter(username=request.POST['Username']).exists():
            # messages.info(request,'Username is already taken')
            message="Username is already taken"
        elif Request.objects.filter(email=request.POST['Email']).exists():
            # messages.info(request,'Email already taken')
            message="Email is already taken"
        else:
            request_details.name = request.POST['Name']
            request_details.username = request.POST['Username']
            request_details.email = request.POST['Email']
            request_details.contact = request.POST['Contact']
            request_details.password = request.POST['Password']
            request_details.country = request.POST['Country']
            
            
            
            if len(request.FILES) != 0:
                request_details.image = request.FILES['image'] 
            
            request_details.save()
            message="Data inserted successfully"
            return render(request,'registration_airlines.html',{'msg':message})
            
            
    return render(request,'registration_airlines.html',{'msg':message})



def searchhome_page(request):
    return render(request,'search_flight_home.html')

def searchcustomer_page(request):
    return render(request,'search_flight_customer.html')

def addflight_page(request):
    return render(request,'add_flight.html')

def mybookings_page(request):
    return render(request,'mybookings.html')

def viewbookings_admin_page(request):
    return render(request,'view_bookings_admin.html')


def viewbookings_airlines_page(request):
    return render(request,'view_bookings_airlines.html')

def viewbookings_admin_details_page(request):
    return render(request,'view_bookings_admin_details.html')

def viewbookings_airlines_details_page(request):
    return render(request,'view_bookings_airlines_details.html')

def viewfeedback_page(request):
    return render(request,'view_feedback.html')

def viewusers_page(request):
    customer_details=Customer.objects.all()
    return render(request,'view_users.html',{'cust':customer_details})

def viewprofile_customer_page(request):
    return render(request,'view_profile_customer.html')

def viewprofile_airlines_page(request):
    return render(request,'view_profile_airlines.html')

def searchresult_home_page(request):
    return render(request,'search_result_home.html')

def searchresult_customer_page(request):
    return render(request,'search_result_customer.html')

def searchresult_detail_home_page(request):
    return render(request,'search_result_detail_home.html')

def searchresult_detail_customer_page(request):
    return render(request,'search_result_detail_customer.html')

def view_flightdetail_admin_page(request):
    return render(request,'view_flight_detail_admin.html')


def view_flight_airlines_page(request):
    return render(request,'view_flight_airlines.html')

def view_airlines_admin_page(request):
    return render(request,'view_airlines_admin.html')

def view_flightdetail_airlines_page(request):
    return render(request,'view_flight_detail_airlines.html')

def edit_flightdetail_airlines_page(request):
    return render(request,'edit_flight_details_airlines.html')

def payment_page(request):
    return render(request,'payment.html')

def add_passenger_page(request):
    return render(request,'add_passenger.html')

def after_booking_page(request):
    return render(request,'after_booking.html')

def view_request_admin_page(request):
    request_details=Request.objects.all()
    return render(request,'view_request_admin.html',{'req':request_details})

def image_upload_page(request):
    return render(request,'image_upload.html')