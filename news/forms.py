from django.forms import ModelForm
from .models import Contact,News,Review


class ContactModelForm(ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']


class NewsModelForm(ModelForm):
    class Meta:
        model=News
        fields=('title','body','image','status','category')

    def __init__(self, *args, **kwargs):
        super(NewsModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        print(self.fields.items())
