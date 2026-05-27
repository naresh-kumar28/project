from django import forms
from blogs.models import Category, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['slug', 'author']


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']