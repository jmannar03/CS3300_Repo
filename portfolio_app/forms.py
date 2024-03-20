from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class PortfolioForm(ModelForm):
    class Meta:
        model=Portfolio
        fields = '__all__'
