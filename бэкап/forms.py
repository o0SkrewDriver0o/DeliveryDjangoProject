from django import forms

from DeliveryDjango.models import Person, Review


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=65)
    password = forms.CharField(label='Пароль', max_length=65, widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput)
    email = forms.EmailField(label='Почта', required=True)
    phone = forms.CharField(label='Номер телефона', max_length=200, required=True)
    name = forms.CharField(label='Имя', max_length=200, required=True)
    lastname = forms.CharField(label='Фамилия', max_length=200, required=True)
    middlename = forms.CharField(label='Отчество', max_length=200, required=True)

    class Meta:
        model = Person
        fields = ['email', 'password1', 'password2', 'phone', 'name', 'lastname', 'middlename']


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=200, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=200, required=True)
    phone_number = forms.CharField(label='Фамилия', max_length=200, required=True)
    address = forms.CharField(label='Адрес для доставки', max_length=200, required=True)
    payment_type = forms.ChoiceField(label='Способ оплаты', choices=[
        ('card', 'Карта'),
        ('cash', 'Наличные'),
    ], required=True)


class ReviewForm(forms.Form):
    review_text = forms.CharField(
        label='Ваш отзыв',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=True
    )
    delivery_speed_rating = forms.IntegerField(
        label='Скорость доставки',
        min_value=1,
        max_value=5,
        required=True
    )
    taste_intensity_rating = forms.IntegerField(
        label='Интенсивность вкуса',
        min_value=1,
        max_value=5,
        required=True
    )
    product_quality_rating = forms.IntegerField(
        label='Качество продукта',
        min_value=1,
        max_value=5,
        required=True
    )

    def save(self, commit=True):
        review = Review(**self.cleaned_data)
        if commit:
            review.save()
        return review
