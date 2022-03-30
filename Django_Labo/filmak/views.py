from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login as auth_login

def index(request):

    return render(request, "filmak/index.html",
                  {
                      'title' : "Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def login(request):
    if request.method == 'POST':
        erabiltzailea = request.POST['erabiltzailea']
        pasahitza = request.POST['pasahitza']
        user = authenticate(username=erabiltzailea, password=pasahitza)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Berbideratu login ondorengo orri batera.
                return HttpResponseRedirect('menua.html')
            else:
                # Errore-mezua bueltatu: 'kontua desgaituta'.
                return render(request, "filmak/login.html",
                {
                    'error' : "Kontua desgaituta."
                    }
                )
        else:
            return render(request, "filmak/login.html",
            {
                'error' : "Login desegokia."
                }
            )
    else:
        form = LoginForm()
        return render(request, "filmak/login.html",
                      {
                          'title' : "Login - Filmak",
                          'message' : "Hello Django!",
                          'content' : "Hello, world. You're at the polls index.",
                          'form' : form
                          }
                      )

def register(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()
        return render(request, "filmak/register.html",
                      {
                          'title' : "Register - Filmak",
                          'message' : "Hello Django!",
                          'content' : "Hello, world. You're at the polls index.",
                          'form' : form
                          }
                      )

def logout(request):

    return render(request, "filmak/logout.html",
                  {
                      'title' : "Logout - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def menua(request):

    return render(request, "filmak/menua.html",
                  {
                      'title' : "Menua - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def bozkatu(request):

    return render(request, "filmak/bozkatu.html",
                  {
                      'title' : "Bozkatu - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def zaleak(request):

    return render(request, "filmak/zaleak.html",
                  {
                      'title' : "Zaleak - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

class LoginForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #Erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE

class RegisterForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #Erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE