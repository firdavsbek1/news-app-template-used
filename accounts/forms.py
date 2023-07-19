from django.forms import ModelForm,PasswordInput,CharField,ValidationError
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.input_type="password"
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            field.widget.attrs.update({'class': 'form-control'})


class UserRegisterForm(ModelForm):
    password1=CharField(label='Password',widget=PasswordInput)
    password2=CharField(label='Password Confirmation',widget=PasswordInput)

    class Meta:
        model = User
        fields= ('username','email')

    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':"input"})
            field.widget.attrs.update({'class':"form-control"})

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] and data['password2']:
            if data['password1'] != data['password2']:
                raise ValidationError('Password mismatch!')
            else:
                return data['password2']
        raise ValidationError('Password field is empty!')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude=('user',)
