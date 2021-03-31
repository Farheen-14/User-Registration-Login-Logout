from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
# def login(request):
#     return render(request,'login.html')
    # return HttpResponse("Hello...")
 
#login form ---
def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word = request.POST['password']
        user=auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Welcome to home page!!!")
            return redirect('script')
        else:
            messages.warning(request,"Invalid email or password! Please try again.")
            return redirect('login')
    else:
        return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        usrr = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        emid = request.POST['email']
        pwd = request.POST['password']
        if User.objects.filter(username=usrr).exists():
            messages.error(request,'Username already exist..Please choose another!')
            return redirect('signup')
        elif User.objects.filter(email=emid).exists():
            messages.error(request,'EmailID already exist..Please choose another!')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=usrr, first_name=fname, last_name=lname, email=emid, password=pwd) #to be continue..
            user.save(); 
            messages.success(request,'User Created, Please LogIn')
            return redirect('login')
    else:
        return render(request,'signup.html') 
        

    # return HttpResponse("Hello...")
def logout(request):
    auth.logout(request)
    messages.success(request,'Please LogIn Again!!!')
    return redirect('/')

def script(request):
    return render(request,'script.html') 

    # return render(request,"{% url 'jsexpl' %}" )