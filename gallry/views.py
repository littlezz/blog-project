from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Gallry
from django.views.generic import ListView, View, FormView
from .forms import ImageForm
# Create your views here.

class GallryListView(ListView):
    model = Gallry
    context_object_name = 'images'
    template_name = 'test_list.html'


class UploadImageView(FormView):
    form_class = ImageForm
    success_url = '/'
    template_name = 'gallry/upload.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

