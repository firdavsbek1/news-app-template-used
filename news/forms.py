from django.forms import ModelForm
from .models import Contact,News


class ContactModelForm(ModelForm):
    class Meta:
        model=Contact
        fields=('name','email','message')


class NewsModelForm(ModelForm):
    class Meta:
        model=News
        fields="__all__"
        exclude=('slug',)

    def __init__(self, *args, **kwargs):
        super(NewsModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})
