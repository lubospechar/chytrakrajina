from django.db import migrations


def copy_advatage_categories_to_temp(apps, schema_editor):
    AdvatageCategory = apps.get_model("catalogue", "AdvatageCategory")
    TempAdvatageCategory = apps.get_model("catalogue", "TempAdvatageCategory")

    temp_advatage_categories = [
        TempAdvatageCategory(
            old_pk=advatage_category.pk,
            advantage_category_cs=advatage_category.advantage_category_cs,
            advantage_category_en=advatage_category.advantage_category_en,
        )
        for advatage_category in AdvatageCategory.objects.all()
    ]

    TempAdvatageCategory.objects.bulk_create(
        temp_advatage_categories,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0036_tempadvatagecategory"),
    ]

    operations = [
        migrations.RunPython(
            copy_advatage_categories_to_temp,
            migrations.RunPython.noop,
        ),
    ]