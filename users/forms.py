from django import forms
from posts.models import Post, Comment, Twister

# from django.forms import ClearableFileInput

class PostForm(forms.ModelForm):
    content = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), required=True)
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',  'placeholder':"Enter post's title"}), required=True)
    about = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter about post'}), required=True)
    content = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}), required=True)

    class Meta:
        model = Post
        fields = ('content', 'title', 'about', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class TwisterForm(forms.ModelForm):
    class Meta:
        model = Twister
        fields = ('body',)

# class EditProfileForm(forms.ModelForm):
#     avatar = forms.ImageField(widget=forms.ImageInput(attrs={'class':'form-control'}), required=True)
#     birthday = forms.DateField(attrs=({'class':'form-control'}), required=True)
#     bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=True)
#     about = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=True)
#
#     class Meta:
#         model = Post
#         fields = ('avatar', 'birthday','bio', 'about')
