from django import forms
from .models import Tracs

class TracsForm(forms.ModelForm):
    class Meta:
        model = Tracs
        fields = ('payer', 'amount', 'item',)
