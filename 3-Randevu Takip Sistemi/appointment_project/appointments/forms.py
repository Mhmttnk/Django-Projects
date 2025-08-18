from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(CustomerUserCreationForm, self).__init__(*args, **kwargs) # Dışarıdan gelen argümanları alır(istek vb). self --> bu formdan oluşacak nesnenin kendisini ifade eder
        for field in self.fields.values(): # fields içindeki tüm değerleri dolaşır
            field.help_text = '' # Yardım metnini kaldırır.
            field.widget.attrs.update({'class': 'form-control'}) #  Her input alanına class="form-control" HTML özelliğini ekler.