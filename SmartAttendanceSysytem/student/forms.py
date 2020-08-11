from django import forms 
from globalapp.models import *

class uploadform(forms.ModelForm): 
  
    class Meta: 
        model = Profile 
        fields = ['head_shot']