from django.forms import ModelForm
from .models import Contact


class ContactModelForm(ModelForm):
    class Meta:
        model=Contact
        fields=('name','email','message')
