from django import forms
from .models import PostModel, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')



class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')
 


class CommentForm (forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add Comment here ... '}))
    class Meta:
        model = Comment
        fields = ('content',)

class CommentUpdateForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Edit Comment here ... '}))
    class Meta:
        model = Comment
        fields = ('content',)