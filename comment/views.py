from django.shortcuts import render
from django.views.generic import View
from .forms import CommentForm
from django.shortcuts import Http404, redirect
from django.apps import apps
# Create your views here.


class CommentView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST

        content_type = data.get('content_type')
        object_pk = data.get('object_pk')

        if not (content_type and object_pk):
            raise Http404

        try:
            model = apps.get_model(content_type)
            target_object = model.objects.get(pk=object_pk)
        except LookupError:
            raise Http404

        cf = CommentForm(target_object, request.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.ip_address = request.META.get('REMOTE_ADDR')
            comment.save()

            return redirect(comment.get_absolute_url)

        else:
            raise Http404
