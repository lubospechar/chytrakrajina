from django.db import models
from django.utils.translation import gettext_lazy as _
from catalogue.fields import ScoreField

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Measure group")
        verbose_name_plural = _("Measure groups")


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

    # score
    temperature = ScoreField(verbose_name=_("Temperature"))
    water = ScoreField(verbose_name=_("Water"))
    biodiversity = ScoreField(verbose_name=_("Biodiversity"))
    air = ScoreField(verbose_name=_("Air"))
    aesthetics = ScoreField(verbose_name=_("Aesthetics"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")

