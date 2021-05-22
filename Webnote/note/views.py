from django.shortcuts import render,redirect
from .models import Note
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='../login')
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        return redirect('createnote')
    my_notes = Note.objects.filter(username__exact = user.username)
    my_notes = my_notes.filter(active__exact = True)
    context = {'notes':my_notes}


    return render(request,'dashboard.html',context)

@login_required(login_url='../login')
def create_note(request):
    user = request.user
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    username = user.username
    newpost = Note(title=title,description = desc,username=username)
    newpost.save()
    return redirect('dashboard')

@login_required(login_url='../login')
def delete_note(request,pk):
    if request.method == 'POST':
        note = Note.objects.get(pk=pk)
        note.delete()
    return redirect('dashboard')
