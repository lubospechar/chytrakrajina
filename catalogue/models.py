import uuid

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from catalogue.fields import ScoreField, ChoiceArrayField
from markdownx.models import MarkdownxField
from django.utils.translation import get_language


class MeasureGroup(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    name_cs = models.CharField(
        max_length=100, verbose_name=_("Measure group name (cs)")
    )

    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Measure group name (en)"),
        null=True,
        blank=True,
    )

    slug_cs = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Measure group slug (cs)"),
    )

    slug_en = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("Measure group slug (en)"),
    )

    short_name_cs = models.CharField(max_length=255,
        verbose_name=_("Measure group short name (cs)"),
    )

    short_name_en = models.CharField(
        verbose_name=_("Measure group short name (en)"),
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
        upload_to="measure_groups", verbose_name=_("Measure group icon")
    )

    ordering = models.IntegerField(default=0, verbose_name=_("Ordering"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))

    def name(self):
        if get_language() == "en":
            return self.name_en
        return self.name_cs

    def description(self):
        if get_language() == "en":
            return self.description_en
        return self.description_cs

    def short_name(self):
        if get_language() == "en":
            return self.short_name_en
        return self.short_name_cs

    def slug(self):
        if get_language() == "en":
            return self.slug_en
        return self.slug_cs

    def measure_count(self):
        return self.measures.count()

    def __str__(self):
        return self.name()

    def save(self, *args, **kwargs):
        self.slug_cs = self.slug_cs or None
        self.slug_en = self.slug_en or None

        if not self.slug_cs and self.name_cs:
            self.slug_cs = slugify(self.name_cs)

        if not self.slug_en and self.name_en:
            self.slug_en = slugify(self.name_en)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Measure group")
        verbose_name_plural = _("Measure groups")
        ordering = ["ordering",]


class LocationType(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
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

    def location_type(self):
        if get_language() == "en":
            return self.location_type_en
        return self.location_type_cs


    def __str__(self):
        return self.location_type_cs

    class Meta:
        verbose_name = _("Location type")
        verbose_name_plural = _("Location types")


class Limitation(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    limitation_cs = models.CharField(max_length=35, verbose_name=_("Limitation (cs)"))
    limitation_en = models.CharField(
        max_length=35, null=True, blank=True, verbose_name=_("Limitation (en)")
    )

    def limitation(self):
        if get_language() == "en":
            return self.limitation_en
        return self.limitation_cs

    def __str__(self):
        return self.limitation_cs

    class Meta:
        verbose_name = _("Limitation")
        verbose_name_plural = _("Limitations")


class AdvatageCategory(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    advantage_category_cs = models.CharField(
        max_length=35, verbose_name=_("Advantage category (cs)")
    )
    advantage_category_en = models.CharField(
        max_length=35, null=True, blank=True, verbose_name=_("Advantage category (en)")
    )

    def __str__(self):
        return self.advantage_category_cs

    def advantage_category(self):
        if get_language() == "en":
            return self.advantage_category_en
        return self.advantage_category_cs

    class Meta:
        verbose_name = _("Advantage category")
        verbose_name_plural = _("Advantage categories")


class Advantage(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    advantage_cs = models.CharField(max_length=35, verbose_name=_("Advantage (cs)"))
    advantage_en = models.CharField(
        max_length=35, null=True, blank=True, verbose_name=_("Advantage (en)")
    )
    advantage_category = models.ForeignKey(
        AdvatageCategory, on_delete=models.CASCADE, verbose_name=_("Advantage category")
    )

    def advantage(self):
        if get_language() == "en":
            return self.advantage_en
        return self.advantage_cs

    def __str__(self):
        return self.advantage_cs

    class Meta:
        verbose_name = _("Advantage")
        verbose_name_plural = _("Advantages")


class PreDesign(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    #TODO: prereqisite czech a english
    prereqisite = models.CharField(max_length=255, verbose_name=_("Prerequisite"))


class SDG(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    sdg_number = models.PositiveSmallIntegerField()
    #TODO: sdg_name czech a english
    sdg_name = models.CharField(max_length=100)
    icon = models.ImageField(null=True, blank=True, upload_to="sdg_icons")

    def __str__(self):
        return self.sdg_name

    class Meta:
        verbose_name = _("Sustainable Development Goal")
        verbose_name_plural = _("Sustainable Development Goals")


class Law(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    description_cs = models.CharField(max_length=100, verbose_name=_("Description (cs)"))
    description_en = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Description (en)")
    )
    url = models.URLField()

    def __str__(self):
        return self.description_cs

    def description(self):
        if get_language() == "en":
            return self.description_en
        return self.description_cs

    class Meta:
        verbose_name = _("Legislation")
        verbose_name_plural = _("Legislations")


class FundingOpportunity(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    description_cs = models.CharField(max_length=100, verbose_name=_("Description (cs)"))
    description_en = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Description (en)")
    )
    url = models.URLField()

    def __str__(self):
        return self.description_cs

    def description(self):
        if get_language() == "en":
            return self.description_en
        return self.description_cs

    class Meta:
        verbose_name = _("Founding opportunity")
        verbose_name_plural = _("Founding opportunities")

class MainProblems(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )
    problem_cs = models.CharField(max_length=100, verbose_name=_("Problem (cs)"))
    problem_en = models.CharField(
        max_length=100, null=True, blank=True, verbose_name=_("Problem (en)")
    )
    icon = models.ImageField(null=True, blank=True, upload_to="main_problems")

    def __str__(self):
        return self.problem_cs

    def problem(self):
        if get_language() == "en":
            return self.problem_en
        return self.problem_cs

    class Meta:
        verbose_name = _("Main problem")
        verbose_name_plural = _("Main problems")

class MeasureCombination(models.Model):
    class DescriptionChoices(models.TextChoices):
        SIMILAR = "similar", _("similar to")
        COMPATIBILE = "compatible", _("compatibile with")
        REQUIRES = "requires", _("requires")

    from_measure = models.ForeignKey(
        "Measure",
        on_delete=models.CASCADE,
        related_name="combination_from",
        verbose_name=_("Measure"),
    )
    to_measure = models.ForeignKey(
        "Measure",
        on_delete=models.CASCADE,
        related_name="combination_to",
        verbose_name=_("Related measure"),
    )

    #TODO: description czech a english
    description = models.CharField(max_length=10, choices=DescriptionChoices, verbose_name=_("Description"), null=True, blank=True)

    def __str__(self):
        return f"{self.from_measure} \u2192 {self.to_measure}"

    class Meta:
        verbose_name = _("Measure combination")
        verbose_name_plural = _("Measure combinations")
        constraints = [
            models.UniqueConstraint(
                fields=["from_measure", "to_measure"],
                name="unique_measure_combination",
            )
        ]


class Measure(models.Model):
    class LMHChoices(models.TextChoices):
        LOW = "L", _("Low")
        MIDDLE = "M", _("Medium")
        HIGH = "H", _("High")

    class SizeChoices(models.TextChoices):
        POINT = "P", _("Point")
        LINE = "L", _("Line")
        AREA = "A", _("Area")

    class MunicipalitySizeChoices(models.TextChoices):
        UP_TO_2000 = "S", _("< 2,000 inhabitants")
        FROM_2000_TO_10000 = "M", _("2,000 – 10,000 inhabitants")
        FROM_10000_TO_50000 = "L", _("10,000 – 50,000 inhabitants")
        OVER_50000 = "XL", _("> 50,000 inhabitants")

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    # base information
    name_cs = models.CharField(max_length=100, verbose_name=_("Measure name (cs)"))

    name_en = models.CharField(
        max_length=100,
        verbose_name=_("Measure name (en)"),
        null=True,
        blank=True,
    )

    slug_cs = models.SlugField(
        max_length=255,
        unique=True,
    )

    slug_en = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(MeasureGroup, verbose_name=_("Measure groups"), related_name="measures")


    location_type = models.ManyToManyField(
        LocationType, verbose_name=_("Location type")
    )

    short_description_cs = models.CharField(
        max_length=255, verbose_name=_("Measure short description (cs)")
    )

    short_description_en = models.CharField(
        max_length=255,
        verbose_name=_("Measure short description (en)"),
        null=True,
        blank=True,
    )

    description_cs = MarkdownxField(_("Measure description (cs)"))

    description_en = MarkdownxField(
        _("Measure description (en)"), null=True, blank=True
    )

    when_and_why_to_use_cs = models.TextField(verbose_name=_("When and why to use (cs)"))
    when_and_why_to_use_en = models.TextField(
        verbose_name=_("When and why to use (en)"), null=True, blank=True
    )

    purpose = models.CharField(max_length=255)

    # score
    temperature = ScoreField(verbose_name=_("Temperature"))
    water = ScoreField(verbose_name=_("Water"))
    biodiversity = ScoreField(verbose_name=_("Biodiversity"))
    air = ScoreField(verbose_name=_("Air"))
    aesthetics = ScoreField(verbose_name=_("Aesthetics"))

    main_advantage = models.ManyToManyField(
        Advantage, verbose_name=_("Main advantage"), related_name="main_advantage"
    )
    advantage = models.ManyToManyField(
        Advantage, verbose_name=_("Advantage"), related_name="advantage"
    )

    municipality_size = ChoiceArrayField(
        models.CharField(max_length=2, choices=MunicipalitySizeChoices),
        default=list,
        blank=True,
        verbose_name=_("Municipality size"),
    )

    main_problems = models.ManyToManyField(MainProblems, verbose_name=_("Main problems"), related_name="main_problems")

    limitation = models.ManyToManyField(Limitation, verbose_name=_("Limitation"))

    complexity_of_realization = models.CharField(
        max_length=1, choices=LMHChoices, verbose_name=_("Complexity of realization")
    )
    budget_choices = models.CharField(
        max_length=1, choices=LMHChoices, verbose_name=_("Budget")
    )

    funding_opportunity = models.ManyToManyField(FundingOpportunity, verbose_name=_("Funding opportunity"), related_name="funding_opportunity", blank=True)

    price = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Price"))
    units = models.CharField(max_length=10, verbose_name=_("Units"))

    time_horizon = models.CharField(
        max_length=1, choices=LMHChoices, verbose_name=_("Time horizon")
    )
    measure_size = models.CharField(
        max_length=1, choices=SizeChoices, verbose_name=_("Measure size")
    )

    diy = models.BooleanField(default=False, verbose_name=_("DIY"))

    combine = models.ManyToManyField(
        "Measure",
        through="MeasureCombination",
        through_fields=("from_measure", "to_measure"),
        symmetrical=False,
        verbose_name=_("Related measures"),
        related_name="related_measures",
        blank=True,
    )

    sdg = models.ManyToManyField(SDG)
    law = models.ManyToManyField(Law)

    def __str__(self):
        return self.name_cs

    def display_groups(self):
        return ", ".join(self.groups.values_list("name_cs", flat=True))
    display_groups.short_description = _("Measure groups")


    def slug(self):
        if get_language() == "cs":
            return self.slug_cs
        else:
            return self.slug_en


    def when_and_why_to_use(self):
        if get_language() == "cs":
            return self.when_and_why_to_use_cs
        else:
            return self.when_and_why_to_use_en

    def name(self):
        if get_language() == "cs":
            return self.name_cs
        else:
            return self.name_en

    def description(self):
        if get_language() == "cs":
            return self.description_cs
        else:
            return self.description_en

    def short_description(self):
        if get_language() == "cs":
            return self.short_description_cs
        else:
            return self.short_description_en

    class Meta:
        verbose_name = _("Measure")
        verbose_name_plural = _("Measures")




class Performance(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("UUID"),
        primary_key=True,
    )

    measure = models.ForeignKey(
        Measure,
        on_delete=models.CASCADE,
    )
    performance = models.CharField(max_length=100, verbose_name=_("Performance"))
