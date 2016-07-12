from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'True',
        }
    ))
    nickname = forms.RegexField(
        label="Nickname", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text="Required. 30 characters or fewer. Letters, digits and "
                  "@/./+/-/_ only.",
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
            "@/./+/-/_ characters."
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nickname',
            'required': 'true',
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password confirmation',
                'required': 'True',
            }
        ),
        help_text="Enter the same password as above, for verification."
    )

    class Meta:
        model = User
        fields = ("email", "nickname", "password1", "password2",)


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'True',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }
        )
    )
