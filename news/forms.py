from django.forms import ModelForm
from .models import Contact,News,Review


class ContactModelForm(ModelForm):
    class Meta:
        model=Contact
        fields=('name','email','message')


class NewsModelForm(ModelForm):
    class Meta:
        model=News
        fields="__all__"
        exclude=('slug','author',)

    def __init__(self, *args, **kwargs):
        super(NewsModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=False):
        """
        Save this form's self.instance object if commit=True. Otherwise, add
        a save_m2m() method to the form which can be called after the instance
        is saved manually at a later time. Return the model instance.
        """
        if self.errors:
            raise ValueError(
                "The %s could not be %s because the data didn't validate."
                % (
                    self.instance._meta.object_name,
                    "created" if self.instance._state.adding else "changed",
                )
            )
        if commit:
            # If committing, save the instance and the m2m data immediately.
            self.instance.save()
            self._save_m2m()
        else:
            # If not committing, add a method to the form to allow deferred
            # saving of m2m data.
            self.save_m2m = self._save_m2m
        return self.instance


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('body',)

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
        print(self.fields.items())
