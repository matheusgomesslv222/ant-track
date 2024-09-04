from django import forms
from .models import UsuarioInfo

class UsuarioInfoCreationForm(forms.ModelForm):
    class Meta:
        model = UsuarioInfo
        fields = ('nome', 'email', 'data_nascimento')
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

class UsuarioInfoChangeForm(forms.ModelForm):
    class Meta:
        model = UsuarioInfo
        fields = ('nome', 'email', 'data_nascimento')
