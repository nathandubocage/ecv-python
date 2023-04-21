from django.shortcuts import render
from .forms import MonFormulaire
import requests


def formulaire(request):
    api_response = None  # Créez une variable pour stocker la réponse de l'API

    if request.method == 'POST':
        form = MonFormulaire(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('http://localhost:9000/api/mon_endpoint', json=data)
            
            if response.status_code == 200:  # Vérifiez que la réponse est valide
                api_response = response.json()  # Traitez la réponse JSON

    else:
        form = MonFormulaire()

    # Passez la réponse de l'API au contexte du template
    return render(request, 'formulaire_app/formulaire.html', {'form': form, 'api_response': api_response})
