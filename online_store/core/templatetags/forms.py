from django import forms
from django.core.exceptions import ValidationError
from ..models import Users
from .custom_censor import checking_words


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            'name',
            'email',
            'password',
            'role'  # Исправил на строчную букву
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте пароль'
            }),
            'role': forms.Select(attrs={  # Исправил на строчную букву
                'class': 'form-control',
                'placeholder': 'Выберите роль'
            }),
        }
        labels = {
            'name': 'Имя',
            'email': 'Почта',
            'password': 'Пароль',
            'role': 'Роль',  # Исправил на строчную букву
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Пожалуйста, введите имя')

        censored_name, has_bad_words = checking_words(name)
        if has_bad_words:
            raise ValidationError(f'Имя содержит запрещённые слова: {censored_name}')

        if len(name) < 2:
            raise ValidationError('Имя слишком короткое! Минимум 2 символа.')
        if len(name) > 40:
            raise ValidationError('Имя слишком длинное! Максимум 40 символов.')
        if name[0].islower():
            raise ValidationError('Имя должно начинаться с заглавной буквы.')

        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError('Пожалуйста, введите email')

        # Проверяем, существует ли пользователь с таким email
        if self.instance.pk:  # если это обновление существующего пользователя
            if Users.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Почта такая уже существует!')
        else:  # если это создание нового пользователя
            if Users.objects.filter(email__iexact=email).exists():
                raise ValidationError('Почта такая уже существует!')

        if len(email) < 5:
            raise ValidationError('Почта слишком короткая! Минимум 5 символов.')
        if len(email) > 40:
            raise ValidationError('Почта слишком длинная! Максимум 40 символов.')

        censored_email, has_bad_words = checking_words(email)
        if has_bad_words:
            raise ValidationError(f'Почта содержит запрещённые слова: {censored_email}')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Пожалуйста, введите пароль')

        if len(password) < 5:
            raise ValidationError('Пароль слишком короткий! Минимум 5 символов.')
        if len(password) > 20:
            raise ValidationError('Пароль слишком длинный! Максимум 20 символов.')

        return password

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data