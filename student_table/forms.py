from django.forms import ModelForm
from . models import student

class studentForm(ModelForm):
    class Meta:
        model = student
        fields = '__all__'