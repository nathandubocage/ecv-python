from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .form import MyForm
import requests

def form(request):
    if request.method == 'POST':
        freetime = request.POST.get('form.freetime')
        traveltime = request.POST.get('form.traveltime')
        health = request.POST.get('form.health')
        absences = request.POST.get('form.absences')
        Walc = request.POST.get('form.Walc')
        Dalc = request.POST.get('form.Dalc')
        goout = request.POST.get('form.goout')
        name = request.POST.get('name')
        age = request.POST.get('age')
        form = MyForm([name, age, freetime, traveltime, health, absences, Walc, Dalc, goout]);
        
        if form.is_valid():
            
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
