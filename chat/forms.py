from django import forms

class ChatMessageForm(forms.Form):
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Type your message...', 'class': 'form-control', 'rows': 2})
    )
