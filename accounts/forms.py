# from attr import field
from unicodedata import category
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import fields
from accounts.models import CustomUser
from django.forms import ModelForm, CharField, TextInput
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from mdeditor.fields import MDTextFormField 
from django.db.models.query_utils import Q

User = get_user_model()

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class UserCreateForm(UserCreationForm):
    check_row = forms.BooleanField(
        label='利用規約',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    class Meta:
        model = User
        fields = ('email','user_id','name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label 

    def clean_email(self):
        email = self.cleaned_data['email']
        User.objects.filter(email=email,is_active=False).delete()
        return email

class UserCreateForm2(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email','user_name','user_id')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class PostCommentForm(forms.Form):
    content = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': '3'}))


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50,)
    user_id = forms.CharField(max_length=10)
    content = forms.CharField(max_length=30,required=False, widget=forms.Textarea(attrs={'rows': '3'}))
    icon = forms.ImageField(widget=forms.widgets.FileInput,required=False)

    instagram = forms.CharField(max_length=200)
    twitter = forms.CharField(max_length=200)
    github = forms.CharField(max_length=200)
    youtube = forms.CharField(max_length=200)
    site = forms.CharField(max_length=200)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label




class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    tel = forms.CharField(min_length=6,max_length=30, label='電話番号',widget=TextInput(attrs={'type':'number'}))
    email = forms.CharField(max_length=30, label='メールアドレス',widget=forms.EmailInput())
    plan = forms.fields.ChoiceField(
        label='問い合わせカテゴリー',
        choices = (
            ('', '---------'),
            ('web', 'Web開発依頼'),
            ('app', 'アプリ開発依頼'),
            ('design', 'デザイン依頼'),
            ('purchase', '写真/素材 買取申請'),
            ('others', 'その他'),
        ),
        required=True,
        widget=forms.widgets.Select
    )
    title = forms.CharField(min_length=2, max_length=100, label='件名')
    text = forms.CharField(min_length=5, max_length=600,label='内容', widget=forms.Textarea())
    remarks = forms.CharField(min_length=5, max_length=600,label='備考', widget=forms.Textarea())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

