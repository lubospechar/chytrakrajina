from django.db import models
from django.utils.translation import gettext_lazy as _
from catalogue.fields import ScoreField
from markdownx.models import MarkdownxField


class MeasureGroup(models.Model):
    name_cs = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name (cs)"))

    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name (en)"),
        null=True, blank=True,
    )

    description_cs = models.TextField(
        verbose_name=_("Measure group description (cs)"),
    )

    description_en = models.TextField(
        verbose_name=_("Measure group description (en)"),
        null=True, blank=True,
    )

    icon = models.ImageField(
        upload_to="measure_groups",
        verbose_name=_("Measure group icon")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Measure group")
        verbose_name_plural = _("Measure groups")


class LocationType(models.Model):
    location_type = models.CharField(max_length=20)


class MainAdvantage(models.Model):
    advantage = models.CharField(max_length=35)


class Limitation(models.Model):
    limitation = models.CharField(max_length=35)


class AdvatageCategory(models.Model):
    advantage_category = models.CharField(max_length=35)


class Advantage(models.Model):
    advantage_category = models.ForeignKey(AdvatageCategory, on_delete=models.CASCADE)
    advantage = models.CharField(max_length=35)


class PreDesign(models.Model):  # predprojektova priprava
    prereqisite = models.CharField(max_length=255)


class SDG(models.Model):
    sdg_number = models.PositiveSmallIntegerField()
    sdg_name = models.CharField(max_length=100)
    icon = models.ImageField()


class Law(models.Model):
    description = models.CharField(max_length=100)
    url = models.URLField


class Measure(models.Model):
    class LMHChoices(models.TextChoices):
        LOW = "L", "Low"
        MIDDLE = "M", "Medium"
        HIGH = "H", "High"

    class SizeChoices(models.TextChoices):
        POINT = "P", "Point"
        LINE = "L", "Line"
        AREA = "A", "Area"

    # base information
    name = models.CharField(
        max_length=100,
        verbose_name=_("Measure name"))

    group = models.ForeignKey(
        MeasureGroup,
        on_delete=models.CASCADE,
        verbose_name=_("Measure group")
    )

    location_type = models.ManyToManyField(LocationType)

    short_description = models.CharField(
        max_length=255,
        verbose_name=_("Measure short description")
    )

    description = MarkdownxField()

    purpose = models.CharField(max_length=255)

    # score
    temperature = ScoreField(verbose_name=_("Temperature"))
    water = ScoreField(verbose_name=_("Water"))
    biodiversity = ScoreField(verbose_name=_("Biodiversity"))
    air = ScoreField(verbose_name=_("Air"))
    aesthetics = ScoreField(verbose_name=_("Aesthetics"))

    main_advantage = models.ManyToManyField(MainAdvantage)
    limitation = models.ManyToManyField(Limitation)

    advantage = models.ManyToManyField(Advantage)

    complexity_of_realization = models.CharField(max_length=1, choices=LMHChoices)
    budget_choices = models.CharField(max_length=1, choices=LMHChoices)

    price = models.PositiveIntegerField()
    units = models.CharField(max_length=10)

    time_horizon = models.CharField(max_length=1, choices=LMHChoices)
    measure_size = models.CharField(max_length=1, choices=SizeChoices)

    diy = models.BooleanField()

    combine = models.ManyToManyField("Measure")

    sdg = models.ManyToManyField(SDG)
    law = models.ManyToManyField(Law)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")


class Performance(models.Model):  # kvantitativni parametry
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    performance = models.CharField(max_length=100)