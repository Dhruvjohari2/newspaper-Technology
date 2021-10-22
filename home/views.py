from django.shortcuts import render , HttpResponse , redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def articles(request):
    return render(request, 'articles.html')    

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")

def daily(request):
    return render(request, 'daily.html')
    # return HttpResponse("This is servicespage")

def weekly(request):
    return render(request, 'weekly.html')
    # return HttpResponse("This is servicespage")    

def views(request):
    return render(request, 'views.html')
    # return HttpResponse("This is servicespage")    


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been successfully recived! ')
    
    return render(request, 'contact.html')
    # return HttpResponse("This is contactpage")

def handleSignup(request):
    if request.method == 'POST':
        #get the post parameters
        username = request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        # Checks for errorneous inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('views')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('views')    
            
        if (pass1 != pass2):
            messages.error(request, "password do not match")
            return redirect('views')


        # create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your account has been successfully created")
        return redirect('views')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully login ")
            return redirect('views')
        else:
            messages.error(request, "Invalid credentials,please try again")
            return redirect('views')    
        
    return HttpResponse('handleLogin')
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    # if request.method == 'POST':
        logout(request)
        messages.success(request, "Successfully logged out")
        return redirect('views')
        # return HttpResponse('handleLogout')