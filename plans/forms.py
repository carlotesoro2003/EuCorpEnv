from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import StrategicGoals, KeyAreas, DepartmentHeads, Lead

class StrategicGoalForm(forms.ModelForm):
    class Meta:
        model = StrategicGoals
        fields = ['name', 'keyArea', 'members', 'leads']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control long-input',
                'placeholder': 'Enter Goal Name',
                'style': 'width: 100%; max-width: 600px; padding: 10px; font-size: 16px;',  
            }),
            'members' : forms.CheckboxSelectMultiple(),
            'leads' : forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(StrategicGoalForm,self).__init__(*args, **kwargs)
        self.fields['keyArea'].queryset = KeyAreas.objects.all()
        self.fields['members'].queryset = DepartmentHeads.objects.all()
        self.fields['leads'].queryset = Lead.objects.all()
