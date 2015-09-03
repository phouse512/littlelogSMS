from django import forms


class SignupAliasForm(forms.Form):
    alias = forms.CharField(max_length=20, required=True)
    email_secret = forms.CharField(max_length=100, required=True)