from django import forms
from account.tasks import activate
from django.contrib.auth.models import User
from settings.settings import HTTP_SCHEMA
from settings.settings import DOMAIN


class Reg_form_class(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("pass not the same")

        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data.get('password1'))
        instance.is_active = False

        activate.delay(f"{HTTP_SCHEMA}://{DOMAIN}/activate/{instance.username}/", instance.email)

        if commit:
            instance.save()
        return instance
