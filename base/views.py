from django.http import JsonResponse
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_sucess_url(self):
        return reverse_lazy('index.html')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index.html')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

from django.http import JsonResponse
from django.shortcuts import render
import requests

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city', 'São Paulo')
        unit = request.GET.get('unit')
        timezone = request.GET.get('timezone', 'America/Sao_Paulo')

        api_url = f"Your server docker link""/api/weather/?city={city}"
        
        response = requests.get(api_url, params={'unit': unit, 'timezone': timezone})

        temperature = None
        timestamp = ''
        error = None

        if response.status_code == 200:
            data = response.json()
            if 'temperature' in data:
                temperature = data['temperature']
                timestamp = data.get('timestamp', '')
            else:
                error = "Data not avalible."
        else:
            error = f"Fail solicitation. Code status: {response.status_code}"

        context = {
            'city': city,
            'unit': unit,
            'temperature': temperature,
            'timestamp': timestamp,
            'error': error,
        }

        return render(request, 'index.html', context)
