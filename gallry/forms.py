from django.forms import ModelForm
from .models import Gallry
__author__ = 'zz'

class ImageForm(ModelForm):
    class Meta:
        model = Gallry
        fields = '__all__'
