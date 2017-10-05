from django import forms


class UploadForm(forms.Form):
    url = forms.CharField(label='Enter a URL: ', max_length=1000)
    pin = forms.CharField(label='Enter a PIN: ', max_length=20)


class PresentForm(forms.Form):
    pin = forms.CharField(label='Enter a PIN: ', max_length=20)
