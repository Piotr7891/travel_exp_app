from django import forms
from .models import COUNTRY, CURRENCY_CHOICES

class AddBusinessTripForm(forms.Form):
    destination = forms.ChoiceField(choices=COUNTRY)
    start_date = forms.DateField()
    end_date = forms.DateField()

class AddExpenseForm(forms.Form):
    description = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)
    expense_image = forms.ImageField(required=False)