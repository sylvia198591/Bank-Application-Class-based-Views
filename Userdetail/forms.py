from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from Userdetail.models import *
from django import forms
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# Sign Up Form

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
class DateInput(forms.DateInput):
    input_type = 'date'
class Profilecreateform(ModelForm):
    # address = forms.CharField(max_length=200, widget=forms.PasswordInput)
    address = forms.CharField(max_length=200, widget=forms.Textarea)
    dob = forms.CharField(widget=DateInput)
    class Meta:

        widgets = {
            'dob': DateInput(),}
        # widgets = {
        #     'Password': forms.PasswordInput(render_value=True),
        # }
        model = Profile
        fields = ["first_name","last_name", "email", "telephone", ]
    def clean(self):
        cleaned_data=super().clean() #mandatory
        first_name=cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        address = cleaned_data.get("address")
        telephone=cleaned_data.get("telephone")
        email=cleaned_data.get("email")
        dob=cleaned_data.get("dob")

class Profilecreateform1(ModelForm):
    # address = forms.CharField(max_length=200, widget=forms.PasswordInput)
    address = forms.CharField(max_length=200, widget=forms.Textarea)
    dob = forms.CharField(widget=DateInput)
    class Meta:

        widgets = {
            'dob': DateInput(),}
        # widgets = {
        #     'Password': forms.PasswordInput(render_value=True),
        # }
        model = Profile
        fields = [ "telephone", ]
    def clean(self):
        cleaned_data=super().clean() #mandatory
        # first_name=cleaned_data.get("first_name")
        # last_name = cleaned_data.get("last_name")
        address = cleaned_data.get("address")
        telephone=cleaned_data.get("telephone")
        # email=cleaned_data.get("email")
        dob=cleaned_data.get("dob")
class RegistrationForm(UserCreationForm):
    # accno=forms.IntegerField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2",]
        wiggets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),
            "password1": forms.PasswordInput(attrs={'class': "form-control"}),
            "password2": forms.PasswordInput(attrs={'class': "form-control"}),
            "password2": forms.PasswordInput(attrs={'class': "form-control"}),
            # "accno": forms.TextInput(attrs={'class': "form-control"}),
        }

class UpdateForm(forms.ModelForm):
    # accno=forms.IntegerField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        wiggets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form - control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),
        }
class cuserForm(forms.ModelForm):
    # accno=forms.IntegerField()
    class Meta:
        model= User
        fields=["username"]
        wiggets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),}

# class EditUserDetailsForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email", "username"]
#         widgets = {
#             "first_name": forms.TextInput(attrs={'class': "form-control"}),
#             "last_name": forms.TextInput(attrs={'class': "form-control"}),
#             "email": forms.EmailInput(attrs={'class': "form-control"}),
#             "username": forms.TextInput(attrs={'class': "form-control"}),

class EditUserDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': "form-control"}),
            "last_name": forms.TextInput(attrs={'class': "form-control"}),
            "email": forms.EmailInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),


        }
