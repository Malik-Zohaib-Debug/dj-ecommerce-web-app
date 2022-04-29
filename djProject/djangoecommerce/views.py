from django.shortcuts import render, HttpResponse
from djangoecommerce.models import RegisteredUser

# Create your views here.
def index(request):
    return render(request, 'base.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def registrationPage(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        firstname = request.POST.get("Firstname")
        lastname = request.POST.get("Lastname")
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        phoneNumber = request.POST.get("PhoneNumber")
        country = request.POST.get("Country")
        state = request.POST.get("State")
        zip = request.POST.get("Zip")
        new_User = RegisteredUser(username=username, firstname=firstname, lastname=lastname, email_address=email, user_address=address, password=password, country=country, state=state, phone_number=phoneNumber, user_zip=zip)
        new_User.save()

    return render(request, 'register.html')
