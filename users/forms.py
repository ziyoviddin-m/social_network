from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'single-field'


class UserRegistrationForm(UserCreationForm):
    CHOICES = (
        ('MALE', 'Мужской'),
        ('FEMALE', 'Женский'),
    )
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Подтвердите пароль"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'single-field'



class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Расскажите о себе'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Сколько вам лет?'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Москва'}))
    job = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Программист'}))
    hobbie = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Играть в футбол, плавать'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Где вы проживаете? Город, ул. дом.'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Тел. номер'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'accept': 'image/*'}))
    cover = forms.ImageField(widget=forms.FileInput(attrs={'type': 'file', 'accept': 'image/*'}), required=False)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'about', 'age', 'city', 'job', 'hobbie', 'address', 'contact', 'image', 'cover')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

