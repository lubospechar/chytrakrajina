# from django.contrib import admin
# from django import forms
# from django.utils.translation import gettext_lazy as _
# from django.core.exceptions import ValidationError
#
# from catalogue.models import (
#     MeasureGroup,
#     Measure,
#     LocationType,
#     Advantage,
#     AdvatageCategory,
#     Limitation,
#     SDG,
#     Law,
# )
#
# class MeasureAdminForm(forms.ModelForm):
#     class Meta:
#         model = Measure
#         fields = "__all__"
#
#     def clean(self):
#         cleaned_data = super().clean()
#
#         main_advantages = cleaned_data.get("main_advantage")
#         advantages = cleaned_data.get("advantage")
#
#         if main_advantages and advantages:
#             advantage_duplicates = main_advantages.filter(
#                 pk__in=advantages.values_list("pk", flat=True)
#             )
#
#             if advantage_duplicates.exists():
#                 raise ValidationError(
#                     _("Main advantage and advantage cannot contain the same items.")
#                 )
#
#         return cleaned_data
#
# @admin.register(SDG)
# class SDGAdmin(admin.ModelAdmin):
#     list_display = ("sdg_number", "sdg_name")
#
# @admin.register(Law)
# class LawAdmin(admin.ModelAdmin):
#     list_display = ("description", "url")
#
# @admin.register(Limitation)
# class LimitationAdmin(admin.ModelAdmin):
#     list_display = ("limitation_cs", "limitation_en")
#
# @admin.register(AdvatageCategory)
# class AdvantageCategoryAdmin(admin.ModelAdmin):
#     list_display = ("advantage_category_cs", "advantage_category_en")
#
# @admin.register(Advantage)
# class MainAdvantageAdmin(admin.ModelAdmin):
#     list_display = ("advantage_cs", "advantage_en", "advantage_category")
#     list_filter = ("advantage_category",)
#
# @admin.register(LocationType)
# class LocationTypeAdmin(admin.ModelAdmin):
#     list_display = ("location_type_cs", "location_type_en")
#
# @admin.register(MeasureGroup)
# class MeasureGroupAdmin(admin.ModelAdmin):
#     list_display = ("name_cs", "name_en", "description_cs", "description_en")
#
# @admin.register(Measure)
# class MeasureAdmin(admin.ModelAdmin):
#     form = MeasureAdminForm
#     list_display = ("name_cs", "short_description_cs", 'group')
#     list_filter = ("group",)
#     search_fields = ("name_cs", "short_description_cs")
#     ordering = ("name_cs",)
#     fieldsets = (
#         (None, {"fields": ("group",)}),
#         (_("Base information (cs)"),
#             {"fields": (
#                 "name_cs",
#                 "short_description_cs",
#                 "description_cs",
#             )},
#         ),
#
#         (_("Base information (en)"),
#             {"fields": (
#                 "name_en",
#                 "short_description_en",
#                 "description_en",
#             )},
#
#         ),
#         (_("Scores"), {"fields": ("aesthetics", "air", "biodiversity", "temperature", "water")}),
#         (_("Additional parameters"), {"fields":  (
#             "location_type",
#             "main_advantage",
#             "advantage",
#             "limitation",
#         )}),
#         (_("Key parameters"), {"fields": ("complexity_of_realization", "budget_choices", "price", "units", "time_horizon", "diy", "measure_size",)}),
#         (_("Legislation"), {"fields": ("law", "sdg",)}),
#         (_("Other"), {"fields": ("combine",)}),
#     )
