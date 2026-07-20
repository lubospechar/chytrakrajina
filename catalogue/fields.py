from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

class ScoreField(models.PositiveSmallIntegerField):
    default = 3
    description = _("Score from 0 to 5")

    default_validators = [
        validators.MinValueValidator(
            0,
            message=_("Score must be at least 0."),
        ),
        validators.MaxValueValidator(
            5,
            message=_("Score must be at most 5."),
        ),
    ]

class ChoiceArrayField(ArrayField):
    """
    ArrayField whose formfield is a MultipleChoiceField (SelectMultiple),
    as long as the base_field defines choices.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)

        # ArrayField.formfield would otherwise override "form_class",
        # so we call Field.formfield directly (bypassing ArrayField.formfield).
        return super(ArrayField, self).formfield(**defaults)