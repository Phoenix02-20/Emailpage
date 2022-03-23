from django import forms

class emailform(forms.Form):
    from_mail = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)
