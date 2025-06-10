import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class NewCommentForm(forms.Form):
    
    description = forms.CharField(
        help_text="Enter a comment about the post.",
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}))
   

    def clean_new_comment(self):
        description_comment = self.cleaned_data['description']

        # Remember to always return the cleaned data.
        return description_comment
