from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'})),
    #is_test = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'})),
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'})),
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'last_login', 'is_superuser', 'is_active', 'date_joined')
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_login'].widget.attrs['class'] = 'form-control'
        self.fields['is_superuser'].widget.attrs['class'] = 'form-check'
        self.fields['is_active'].widget.attrs['class'] = 'form-check'
        self.fields['date_joined'].widget.attrs['class'] = 'form-control'

class PasswordChangingForm(PasswordChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'})),
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})),

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.EmailField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'})),
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'})),
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'})),

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'




