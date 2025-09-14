from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'login__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'login__input'}))
    gmail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'login__input'}))