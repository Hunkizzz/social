from django import forms
from social_content.models import Content

class ContentCreateForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ('title','image', 'entry',)

class DeleteContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = []