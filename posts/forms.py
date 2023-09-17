from django import forms
from django.forms import FileInput, ModelForm, Textarea

from posts.models import Post


class CreatePostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'accept': 'image/*'}), required=False)
    video = forms.FileField(widget=forms.FileInput(attrs={'accept': 'video/*'}), required=False)

    class Meta:
        model = Post
        fields = ['description', 'image', 'video']
        
