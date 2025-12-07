from django import forms
from .models import Expenses

class ExpenseForm(forms.ModelForm):
    long_term = forms.BooleanField(required=False)

    class Meta:
        model = Expenses
        fields = ['name', 'amount', 'interest_rate', 'date', 'end_date', 'long_term']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'long_term': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        long_term = cleaned_data.get("long_term")

        if long_term:
            # User selected long-term expense
            pass
        else:
            cleaned_data['end_date'] = None
            cleaned_data['interest_rate'] = None

        return cleaned_data
