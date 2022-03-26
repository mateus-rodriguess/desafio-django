from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import Profile, User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Email...',}))
    username = forms.CharField(min_length=6, max_length=24,
                               widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
   
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
      
    def clean_email(self):
        ValidationEmail = self.cleaned_data['email']

        if User.objects.filter(email=ValidationEmail).exists():
            raise ValidationError(f"O email {ValidationEmail} ja esta em uso")
        return ValidationEmail

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(f"Username {username} ja esta em uso.")

  
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome...',}), label="Primeiro nome")
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Sobrenome...',}), label="Sobrenome")
    
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')

    
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
    
