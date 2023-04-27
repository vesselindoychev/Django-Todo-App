from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value should contains only letters!')


def validate_title(value):
    symbols = [' ', "'", ',', '.', '!']
    for ch in value:
        if ch.isalpha() or ch in symbols:
            continue
        raise ValidationError('Value should contains only letters and symbols!')
