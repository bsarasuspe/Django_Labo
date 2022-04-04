from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout

from filmak.models import Filma

def index(request):

    return render(request, "filmak/index.html",
                  {
                      'title' : "Filmak",
                      }
                  )

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        erabiltzailea = request.POST['erabiltzailea']
        pasahitza = request.POST['pasahitza']
        user = authenticate(username=erabiltzailea, password=pasahitza)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                # Berbideratu login ondorengo orri batera.
                return HttpResponseRedirect('menua')
            else:
                # Errore-mezua bueltatu: 'kontua desgaituta'.
                return render(request, "filmak/login.html",
                {
                    'title' : "Login - Filmak",
                    'form' : form,
                    'message' : "Kontua desgaituta."
                    }
                )
        else:
            return render(request, "filmak/login.html",
            {
                'title' : "Login - Filmak",
                'form' : form,
                'message' : "Login desegokia."
                }
            )
    else:
        return render(request, "filmak/login.html",
                      {
                          'title' : "Login - Filmak",
                          'form' : form
                          }
                      )

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        erabiltzailea = request.POST['erabiltzailea']
        eposta = request.POST['eposta']
        pasahitza = request.POST['pasahitza']
        try:
            erab = User.objects.create_user(erabiltzailea, eposta, pasahitza)
        except:
            return render(request, "filmak/register.html",
            {
                'title' : "Register - Filmak",
                'message' : "Erabiltzaile izen hori dagoeneko erregistratuta dago.",
                'form' : form
                }
            )
        else:
            return render(request, "filmak/register.html",
            {
                'title' : "Register - Filmak",
                'message' : "Ongi erregistratu zara!",
                'form' : form
                }
            )
    else:
        return render(request, "filmak/register.html",
                      {
                          'title' : "Register - Filmak",
                          'form' : form
                          }
                      )

def menua(request):

    return render(request, "filmak/menua.html",
                  {
                      'title' : "Menua - Filmak",
                      }
                  )

def logout(request):

    logout(request)
    return HttpResponseRedirect('')


def filmakIkusi(request):

    filmak = Filma.objects.all()
    paginator = Paginator(filmak, 5) 

    return render(request, "filmak/filmakIkusi.html",
                  {
                      'title' : "Menua - Filmak",
                      'content' = paginator.page(1)
                      }
                  )

def bozkatu(request):

    return render(request, "filmak/bozkatu.html",
                  {
                      'title' : "Bozkatu - Filmak",
                      }
                  )

def zaleak(request):

    return render(request, "filmak/zaleak.html",
                  {
                      'title' : "Zaleak - Filmak",
                      }
                  )

class LoginForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #Erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE

class RegisterForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #pasahitza
    errepPasahitza = forms.CharField(widget=forms.PasswordInput, max_length=100, required=True) #errepikatu pasahitza

    