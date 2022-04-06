from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required as login_required

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
        pasahitza = request.POST['pasahitza']
        pasahitza2 = request.POST['pasahitza2']
        if (pasahitza == pasahitza2):
            try:
                erab = User.objects.create_user(username=erabiltzailea, password=pasahitza)
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
                          'message' : "Pasahitzak ez dira berdinak!",
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

@login_required(login_url='')
def menua(request):

    return render(request, "filmak/menua.html",
                  {
                      'title' : "Menua - Filmak",
                      }
                  )

@login_required(login_url='')
def logout(request):

    logout(request)
    return render(request, "filmak/index.html",
                  {
                      'title' : "Filmak",
                      }
                  )
    #return HttpResponseRedirect('')

@login_required(login_url='')
def filmakIkusi(request):

    filmak = Filma.objects.all()
    paginator = Paginator(filmak, 4) #taulan aldi berean gehienez 4 film erakusteko.

    page = request.GET.get('page') #filmakIkusi.html-k eskatutako orriaren zenbakia jasotzen du.

    try:
        filmList = paginator.page(page)
    except PageNotAnInteger: #jasotako "page" ez bada Integer bat, lehenengo orria itzuliko da.
        filmList = paginator.page(1)
    except EmptyPage: #jasotako "page" filmen orri kopurua baino handiagoa bada, azken orria itzuliko da.
        filmList = paginator.page(paginator.num_pages)


    return render(request, "filmak/filmakIkusi.html",
                  {
                      'title' : "Menua - Filmak",
                      'content' : filmList
                      }
                  )

@login_required(login_url='')
def bozkatu(request):

    filmak = Filma.objects.all()
    if request.method == 'POST':
        aukera = request.POST['filmak']
        return render(request, "filmak/bozkatu.html",
                  {
                      'title' : "Bozkatu - Filmak",
                      'filmak' : filmak,
                      'mezua1' : "Bozkaketa ongi burutu da",
                      'mezua2' : "Zure bozka: " + aukera,
                      }
                  )
    else:
        return render(request, "filmak/bozkatu.html",
                  {
                      'title' : "Bozkatu - Filmak",
                      'filmak' : filmak,
                      }
                  )

        
    
    

@login_required(login_url='')
def zaleak(request):

    filmak = Filma.objects.all()

    return render(request, "filmak/zaleak.html",
                  {
                      'title' : "Zaleak - Filmak",
                      'filmak' : filmak
                      }
                  )

class LoginForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #Erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE

class RegisterForm(forms.Form): #Manualki login formularioa
    erabiltzailea = forms.CharField(max_length=100, required=True) #Erabiltzaile izena
    pasahitza = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE
    pasahitza2 = forms.CharField(widget=forms.PasswordInput, required=True) #defektuz required beti da TRUE

    