from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,  login as loginWork, logout
from django.contrib.auth.decorators import login_required
from .forms import NotesForm


def login(r):
    form = AuthenticationForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            account = authenticate(username=username,password=password)
            if account is not None:
                loginWork(r, account)
                return redirect(homepage)
            else:
                print("username and password invalid")
        else:
            print("not valid form")
    return render(r,"accounts/login.html",{"form":form})

def register(r):
    form = UserCreationForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(login)
    return render(r,"accounts/register.html",{"form":form})


@login_required()
def homepage(r):
    form = NotesForm(r.POST or None)
    data = {"form":form}
    return render(r,"home.html",data)


def logout_view(r):
    logout(r)
    return redirect(homepage)