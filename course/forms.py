from django import forms
from course.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'cols': 100}),
            'rating': forms.RadioSelect,
        }
