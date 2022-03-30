from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):

    return render(request, "filmak/index.html",
                  {
                      'title' : "Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def login(request):

    return render(request, "filmak/login.html",
                  {
                      'title' : "Login - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )

def register(request):

    return render(request, "filmak/register.html",
                  {
                      'title' : "Register - Filmak",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
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