from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    user_id = forms.CharField(label='ユーザーID', max_length=30, required=True)
    email = forms.EmailField(label='メールアドレス',required=True)
    name = forms.CharField(label="名前", max_length=30, required=False)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('user_id','password1','password2', 'email', 'name')
        labels = {
            'user_id': 'ユーザーID',
            'password1': 'パスワード',
            'password2': 'パスワード（確認用）',
            'email': 'メールアドレス',
            'name': '名前',
        }
        help_texts = {"username": None,}