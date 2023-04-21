from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .form import MyForm
import requests
import json

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
                'age': int(age),
                'freetime': int(freetime),
                'traveltime': int(traveltime),
                'health': int(health),
                'absences': int(absences),
                'Walc': int(Walc),
                'Dalc': int(Dalc),
                'goout': int(goout),
            }

            # headers = {'Content-Type': 'application/json'}
            # url = 'http://localhost:8000/predict'
            # response = requests.post(url, data=json.dumps(form_data), headers=headers)

            # if response.status_code == 200:
            #     print('Requête envoyée avec succès')
            #     return render(request, 'prediction.html', {'data': response.json()})
            # else:
            #     print('Erreur lors de l\'envoi de la requête:', response.status_code)

            return render(request, 'prediction.html', {'data': {"prediction": 3.0}})

            
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = MyForm()
        return render(request, 'form.html', {'form': form})
