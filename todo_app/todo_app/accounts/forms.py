import datetime

from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from todo_app.accounts.models import Profile
from todo_app.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class EditProfileForm(forms.ModelForm):
    class Meta:
        YEARS = [i for i in range(1960, int(datetime.date.today().year) + 1)]
        model = Profile
        exclude = ('user',)
        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=YEARS,
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis egestas maecenas pharetra convallis posuere morbi leo. Tincidunt arcu non sodales neque sodales ut. Imperdiet proin fermentum leo vel. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio. Aliquet nec ullamcorper sit amet risus nullam eget felis eget. Orci eu lobortis elementum nibh. Pellentesque elit eget gravida cum sociis natoque. Ultricies leo integer malesuada nunc vel risus commodo viverra maecenas. Pharetra massa massa ultricies mi quis hendrerit. In metus vulputate eu scelerisque.'
                }
            )
        }


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter first name'}
        ),
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter last name'}
        ),
    )

    picture = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'Enter URL'}
        ),
        label='Link to Profile Picture',
    )

    gender = forms.CharField(
        widget=forms.Select(
            choices=((g, g) for g in Profile.GENDERS),
        )

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'gender',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email'
                }
            )
        }
