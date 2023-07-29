from .models import Contact, Comment
from django import forms

# ModelForm dan foydalandik
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')

# Form dan foydalanish
# MISOL
#class SendMessageForm(forms.Form):
#    name=forms.CharField(label="Your name",max_length=150)
#    text=forms.TextInput()
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
