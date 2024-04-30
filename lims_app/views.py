from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return HttpResponse("Hello world. You're at the home page.")
