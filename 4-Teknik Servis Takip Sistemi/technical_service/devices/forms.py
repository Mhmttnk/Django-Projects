from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length = 11, required = True, label = 'phone_number')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomerUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

    def save(self, commit = True):
        user = super().save(commit = False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user                

# Formda göstermek istediğimiz bir alan, modelde hazır olarak yoksa o alanı kendimiz sınıf içerisinde field olarak tanımlarız.             