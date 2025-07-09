# internal_chat/forms.py

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'file']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Type your message...',
                'class': 'chat-input',
                'style': 'resize:none; width:100%;'
            }),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and file.size > 2 * 1024 * 1024:
            raise forms.ValidationError("File too large (max 2MB).")
        return file
