from django import forms

from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.models import User

class signupform(UserChangeForm):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)


    class meta:
        model =User
        fields =('username','password','password1','password2','first_name','last_name')



    def save(self,commit=True):
        user =super(signupform,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['email']
        user.last_name = self.cleaned_data['email']



        if commit:

            user.save()
        return user


