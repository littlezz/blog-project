from django import forms
from .models import Comment
from django.utils.timezone import now
__author__ = 'zz'


class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    website = forms.URLField(required=False)


class CommentForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_pk = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ('username', 'email', 'website', 'content')
        help_texts = {
            'username': '*',
            'content': '*',
        }

    def __init__(self, target_object, *args, **kwargs):
        self.target_object = target_object
        initial = {
            'content_type': str(target_object._meta),
            'object_pk': str(target_object.id)
        }
        kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

    def save(self, commit=True):

        comment = super().save(commit=False)
        comment.content_object = self.target_object

        old = self.check_duplicate(comment)
        if old:
            return old

        if commit:
            comment.save()
        return comment

    def check_duplicate(self, new):
        possible_dup = self.Meta.model.objects.filter(
            username=new.username,
            content_type=new.content_type,
            object_id=new.object_id,
            email=new.email,
            website=new.website,
        )
        print(new.create_time)
        for old in possible_dup:
            if old.create_time.date() == now().date() and old.content == new.content:
                return old




