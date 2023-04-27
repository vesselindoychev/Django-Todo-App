from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Task(models.Model):
    TITLE_MAX_LENGTH = 50
    TITLE_MIN_LENGTH = 2

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        validators=(
            MinLengthValidator(TITLE_MIN_LENGTH),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    complete = models.BooleanField(
        default=False,
    )

    create = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('complete', )