from django import forms
from .models import Star


class SystemForm(forms.Form):
    name = forms.CharField(label='System Name', max_length=100)

class StarForm(forms.ModelForm):
    system_name = forms.CharField(max_length=100, required=True, label='System Name')

    class Meta:
        model = Star
        fields = ['name', 'distance', 'system_name']
        labels = {
            'name': 'Name',
            'distance': 'Distance to Earth (light-years)',
            'system_name': 'System Name',
        }
class SearchForm(forms.Form):
    star_name = forms.CharField(label='Search Star', max_length=100, required=False)
