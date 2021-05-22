from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from note.models import Note
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password =password)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')

        else:
            messages.info(request,'Incorrect credentials')

    return render(request,'login.html')

def register(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        if form.is_valid():

            note = Note(title="Dummy note title",description = "Dummy note description",username = username,active = True)
            note.save()
            form.save()

            messages.success(request,'Your account has been created')
            return redirect('login')

    return render(request,'register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')
