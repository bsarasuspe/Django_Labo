from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):

    return render(request, "filmak/index.html",
                  {
                      'title' : "Hello Django",
                      'message' : "Hello Django!",
                      'content' : "Hello, world. You're at the polls index."
                      }
                  )