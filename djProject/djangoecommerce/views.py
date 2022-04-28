from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')

def loginPage(request):
    return render(request, 'loginPage.html')

def registrationPage(request):
    return render(request, 'register.html')

