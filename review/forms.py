from django import forms
from .models import Post, Comment
from django_summernote import fields as summer_fields
from .models import SummerNote
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    #fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
    class Meta:
        model = Post
        fields = ['title','content','photo','tags','tag_set','hits',]
        widgets = {
            'hits' : forms.HiddenInput,
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author','message']

    def clean_message(self):
        return self.cleaned_data.get('message','').strip()