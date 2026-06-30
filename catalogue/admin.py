from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from catalogue.models import (
    MeasureGroup,
    Measure,
    LocationType,
)

@admin.register(LocationType)
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ("location_type_cs", "location_type_en")

@admin.register(MeasureGroup)
class MeasureGroupAdmin(admin.ModelAdmin):
    list_display = ("name_cs", "name_en", "description_cs", "description_en")

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ("name_cs", "short_description_cs", 'group')
    list_filter = ("group",)
    search_fields = ("name_cs", "short_description_cs")
    ordering = ("name_cs",)
    fieldsets = (
        (None, {"fields": ("group",)}),
        (_("Base information (cs)"),
            {"fields": (
                "name_cs",
                "short_description_cs",
                "description_cs",
            )},
        ),

        (_("Base information (en)"),
            {"fields": (
                "name_en",
                "short_description_en",
                "description_en",
            )},

        ),
        (_("Scores"), {"fields": ("aesthetics", "air", "biodiversity", "temperature", "water")}),
        (_("Additional parameters"), {"fields":  ("location_type", )}),
    )
