from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from budget.models import CustomUser


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control ', 'placeholder': 'Please enter your first name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your last name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['gender'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please select your gender'})
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please select your day of birth'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please repeat your password'})


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Please enter your username"
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': "Please enter your password"
        })