from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from todo_app.accounts.managers import TodoAppUserManager
from todo_app.common.custom_validators import validate_only_letters


class TodoAppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = TodoAppUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDERS = (
        MALE,
        FEMALE,
        OTHER,
    )

    # REQUIRED FIELDS

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    gender = models.CharField(
        max_length=(max(len(gender) for gender in GENDERS)),
        choices=((gender, gender) for gender in GENDERS),
    )

    # UNREQUIRED FIELDS

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    user = models.OneToOneField(
        TodoAppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
