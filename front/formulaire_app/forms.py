from django import forms

class MonFormulaire(forms.Form):
    champ1 = forms.CharField(label="Champ 1", max_length=100)
    champ2 = forms.IntegerField(label="Champ 2")
    # Ajoutez d'autres champs si nécessaire