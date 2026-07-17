import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from catalogue.fields import ScoreField
from markdownx.models import MarkdownxField


class TempMesureGroup(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    old_pk = models.PositiveIntegerField(unique=True, verbose_name=_("Old primary key"))

    name_cs = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name (cs)")
    )

    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name (en)"),
        null=True,
        blank=True,
    )

    description_cs = models.TextField(
        verbose_name=_("Measure group description (cs)"),
    )

    description_en = models.TextField(
        verbose_name=_("Measure group description (en)"),
        null=True,
        blank=True,
    )

    icon = models.ImageField(
        upload_to="temp_measure_groups",
        verbose_name=_("Measure group icon")
    )

    def __str__(self):
        return self.name_cs

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
        return self.name_cs

    class Meta:
        verbose_name = _("Measure group")
        verbose_name_plural = _("Measure groups")


class TempLocationType(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    old_pk = models.PositiveIntegerField(
        unique=True,
        verbose_name=_("Old primary key"),
    )

    location_type_cs = models.CharField(
        max_length=20,
        verbose_name=_("Location type (cs)"),
    )

    location_type_en = models.CharField(
        max_length=20,
        verbose_name=_("Location type (en)"),
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.location_type_cs


class LocationType(models.Model):
    location_type_cs = models.CharField(max_length=20, verbose_name=_("Location type (cs)"))
    location_type_en = models.CharField(max_length=20, verbose_name=_("Location type (en)"), null=True, blank=True)

    def __str__(self):
        return self.location_type_cs

    class Meta:
        verbose_name = _("Location type")
        verbose_name_plural = _("Location types")


class TempLimitation(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )
    old_pk = models.PositiveIntegerField(unique=True, verbose_name=_("Old primary key"))
    limitation_cs = models.CharField(max_length=35, verbose_name=_("Limitation (cs)"))
    limitation_en = models.CharField(max_length=35, null=True, blank=True, verbose_name=_("Limitation (en)"))


class Limitation(models.Model):
    limitation_cs = models.CharField(max_length=35, verbose_name=_("Limitation (cs)"))
    limitation_en = models.CharField(max_length=35, null=True, blank=True, verbose_name=_("Limitation (en)"))

    def __str__(self):
        return self.limitation_cs

    class Meta:
        verbose_name = _("Limitation")
        verbose_name_plural = _("Limitations")


class AdvatageCategory(models.Model):
    advantage_category_cs = models.CharField(max_length=35, verbose_name=_("Advantage category (cs)"))
    advantage_category_en = models.CharField(max_length=35, null=True, blank=True, verbose_name=_("Advantage category (en)"))

    def __str__(self):
        return self.advantage_category_cs

    class Meta:
        verbose_name = _("Advantage category")
        verbose_name_plural = _("Advantage categories")


class Advantage(models.Model):
    advantage_cs = models.CharField(max_length=35)
    advantage_en = models.CharField(max_length=35, null=True, blank=True)
    advantage_category = models.ForeignKey(AdvatageCategory, on_delete=models.CASCADE, verbose_name=_("Advantage category"))

    def __str__(self):
        return self.advantage_cs

    class Meta:
        verbose_name = _("Advantage")
        verbose_name_plural = _("Advantages")

class PreDesign(models.Model):  # predprojektova priprava
    prereqisite = models.CharField(max_length=255)


class SDG(models.Model):
    sdg_number = models.PositiveSmallIntegerField()
    sdg_name = models.CharField(max_length=100)
    icon = models.ImageField(null=True, blank=True, upload_to="sdg_icons")

    def __str__(self):
        return self.sdg_name

    class Meta:
        verbose_name = _("Sustainable Development Goal")
        verbose_name_plural = _("Sustainable Development Goals")


class Law(models.Model):
    description = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("Legislation")
        verbose_name_plural = _("Legislations")


class Measure(models.Model):
    class LMHChoices(models.TextChoices):
        LOW = "L", _("Low")
        MIDDLE = "M", _("Medium")
        HIGH = "H", _("High")

    class SizeChoices(models.TextChoices):
        POINT = "P", _("Point")
        LINE = "L", _("Line")
        AREA = "A", _("Area")

    # base information
    name_cs = models.CharField(
        max_length=100,
        verbose_name=_("Measure name (cs)")
    )

    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Measure name (en)"),
        null=True, blank=True,
    )

    group = models.ForeignKey(
        MeasureGroup,
        on_delete=models.CASCADE,
        verbose_name=_("Measure group")
    )

    location_type = models.ManyToManyField(LocationType, verbose_name=_("Location type"))

    short_description_cs = models.CharField(
        max_length=255,
        verbose_name=_("Measure short description (cs)")
    )

    short_description_en = models.CharField(
        max_length=255,
        verbose_name=_("Measure short description (en)"),
        null=True, blank=True,
    )

    description_cs = MarkdownxField(_("Measure description (cs)"))

    description_en = MarkdownxField(_("Measure description (en)"), null=True, blank=True)

    purpose = models.CharField(max_length=255)

    # score
    temperature = ScoreField(verbose_name=_("Temperature"))
    water = ScoreField(verbose_name=_("Water"))
    biodiversity = ScoreField(verbose_name=_("Biodiversity"))
    air = ScoreField(verbose_name=_("Air"))
    aesthetics = ScoreField(verbose_name=_("Aesthetics"))

    main_advantage = models.ManyToManyField(Advantage, verbose_name=_("Main advantage"), related_name="main_advantage")
    advantage = models.ManyToManyField(Advantage, verbose_name=_("Advantage"), related_name="advantage")

    limitation = models.ManyToManyField(Limitation, verbose_name=_("Limitation"))



    complexity_of_realization = models.CharField(max_length=1, choices=LMHChoices, verbose_name=_("Complexity of realization"))
    budget_choices = models.CharField(max_length=1, choices=LMHChoices, verbose_name=_("Budget"))

    price = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Price"))
    units = models.CharField(max_length=10, verbose_name=_("Units"))

    time_horizon = models.CharField(max_length=1, choices=LMHChoices, verbose_name=_("Time horizon"))
    measure_size = models.CharField(max_length=1, choices=SizeChoices, verbose_name=_("Measure size"))

    diy = models.BooleanField(default=False, verbose_name=_("DIY"))

    combine = models.ManyToManyField("Measure", verbose_name=_("Related measures"), related_name="related_measures", blank=True,)

    sdg = models.ManyToManyField(SDG)
    law = models.ManyToManyField(Law)

    def __str__(self):
        return self.name_cs

    class Meta:
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")


class Performance(models.Model):  # kvantitativni parametry
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)
    performance = models.CharField(max_length=100)