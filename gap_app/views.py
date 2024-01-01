from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import View
import joblib
from .forms import *
import pickle


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    return render(request, "registration.html", {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        us = request.POST['username']
        ps = request.POST['password']
        if us is not None and ps is not None:
            user = authenticate(request, username=us, password=ps)
            if user:
                login(request, user)
                return redirect('gap')
    return render(request, 'login.html', {'form': form})

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('')



def get_output(list_data):
    model = joblib.load("gap_app/Global_air_polution.sav")
    prediction = model.predict([list_data])
    return prediction

def gap(request):
    form = GlobalAirPolutionForm()
    if request.method == "POST":
        form = GlobalAirPolutionForm(request.POST)
        if form.is_valid():
            form.save()
            aqi = form.cleaned_data['aqi']
            co_aqi = form.cleaned_data['co_aqi']
            ozone_aqi = form.cleaned_data['ozone_aqi']
            no2_aqi = form.cleaned_data['no2_aqi']
            pm2_5_aqi = form.cleaned_data['pm2_5_aqi']

            list_data = [aqi, co_aqi, ozone_aqi, no2_aqi, pm2_5_aqi
                         ]
            data = get_output(list_data)
            output = ''
            if data[0] == 0:
                output = 'result0'
            elif data[0] == 1:
                output = 'result1'
            elif data[0] == 2:
                output = 'result2'
            elif data[0] == 3:
                output = 'result3'
            elif data[0] == 4:
                output = 'result4'
            else:
                output = 'result5'
            return redirect('output', output)
    return render(request, "Gap.html", {'form': form})


def output(request, rs):
    result = ''
    if rs == 'result0':
        result = 0
    elif rs == 'result1':
        result = 1
    elif rs == 'result2':
        result = 2
    elif rs == 'result3':
        result = 3
    elif rs == 'result4':
        result = 4
    elif rs == 'result5':
        result = 5

    return render(request, "output.html",{'result':result})