from django import forms


class CreateUserForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(min_length=5)
    confirm_password = forms.CharField(min_length=5)

