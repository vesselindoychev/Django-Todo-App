from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value should contains only letters!')


def validate_title(value):
    for ch in value:
        if ch.isalpha() or ch == '':
            continue
        raise ValidationError('Value should contains only letters!')
