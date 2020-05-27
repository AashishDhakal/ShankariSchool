from django import forms
from .models import ParentInformation

class ParentInformationForm(forms.ModelForm):
    class Meta:
        model = ParentInformation
        fields = '__all__'