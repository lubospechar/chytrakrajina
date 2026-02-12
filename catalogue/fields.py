from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

class ScoreField(models.PositiveSmallIntegerField):
    default = 3
    description = _("Score from 0 to 5")

    default_validators = [
        validators.MinValueValidator(
            0,
            message=_("Score must be at least %(limit_value)s."),
        ),
        validators.MaxValueValidator(
            5,
            message=_("Score must be at most %(limit_value)s."),
        ),
    ]