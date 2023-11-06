from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(label='Email')
    full_name = forms.CharField(max_length=255, label='Full Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    country = forms.CharField(max_length=100, label='Country')
    mobile_number = forms.CharField(max_length=20, label='Mobile Number')
    identity_document = forms.FileField(label='Identity Document', required=False)
