from django import forms

from.models import Comments, Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'url')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)