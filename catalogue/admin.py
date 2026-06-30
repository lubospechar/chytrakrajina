from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from catalogue.models import (
    MeasureGroup,
    Measure
)

@admin.register(MeasureGroup)
class MeasureGroupAdmin(admin.ModelAdmin):
    list_display = ("name_cs", "name_en", "description_cs", "description_en")

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description")
    list_filter = ("group",)
    search_fields = ("name", "short_description")
    ordering = ("name",)
    fieldsets = (
        (_("Base information"), {"fields": ("name", "short_description", "group")}),
        (_("Scores"), {"fields": ("aesthetics", "air", "biodiversity", "temperature", "water")}),
    )
