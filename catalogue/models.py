from django.db import models
from django.utils.translation import gettext_lazy as _


class MeasureGroup(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name"))

    description = models.TextField(
        verbose_name=_("Measure group description"))

    icon = models.ImageField(
        upload_to="measure_groups",
        verbose_name=_("Measure group icon")
    )


class Measure(models.Model):
    # base information
    name = models.CharField(
        max_length=100,
        verbose_name=_("Measure name"))

    group = models.ForeignKey(
        MeasureGroup,
        on_delete=models.CASCADE,
        verbose_name=_("Measure group")
    )

    short_description = models.CharField(
        max_length=255,
        verbose_name=_("Measure short description")
    )
