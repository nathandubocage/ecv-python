from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=15, max_value=22)
    freetime = forms.IntegerField(min_value=1, max_value=5)
    traveltime = forms.IntegerField(min_value=1, max_value=4)
    health = forms.IntegerField(min_value=1, max_value=5)
    absences = forms.IntegerField(min_value=0, max_value=93)
    Walc = forms.IntegerField(min_value=1, max_value=5)
    Dalc = forms.IntegerField(min_value=1, max_value=5)
    goout = forms.IntegerField(min_value=1, max_value=5)



# age - student's age (numeric: from 15 to 22)
# freetime - free time after school (numeric: from 1 - very low to 5 - very high)
# traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
# health - current health status (numeric: from 1 - very bad to 5 - very good)
# absences - number of school absences (numeric: from 0 to 93)
# Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
# Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
# goout - going out with friends (numeric: from 1 - very low to 5 - very high)
