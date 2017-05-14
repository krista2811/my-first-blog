from django import forms
from .models import Post, Comment
from django.forms import ModelForm

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('name', 'description',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

