from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .form import MyForm
import requests

def form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        
        if form.is_valid():
            age = form.cleaned_data['age']
            freetime = form.cleaned_data['freetime']
            traveltime = form.cleaned_data['traveltime']
            health = form.cleaned_data['health']
            absences = form.cleaned_data['absences']
            Walc = form.cleaned_data['Walc']
            Dalc = form.cleaned_data['Dalc']
            goout = form.cleaned_data['goout']

            form_data = {
                'age': age,
                'freetime': freetime,
                'traveltime': traveltime,
                'health': health,
                'absences': absences,
                'Walc': Walc,
                'Dalc': Dalc,
                'goout': goout,
            }

            url = 'http://example.com/form'
            response = requests.post(url, data=form_data)

            if response.status_code == 200:
                print('Requête envoyée avec succès')
            else:
                print('Erreur lors de l\'envoi de la requête:', response.status_code)

            return HttpResponse('Form submitted successfully!')
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = MyForm()
        return render(request, 'form.html', {'form': form})
