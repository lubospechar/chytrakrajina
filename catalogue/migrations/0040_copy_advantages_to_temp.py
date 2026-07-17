from django.db import migrations


def copy_advantages_to_temp(apps, schema_editor):
    Advantage = apps.get_model("catalogue", "Advantage")
    TempAdvantage = apps.get_model("catalogue", "TempAdvantage")
    TempAdvatageCategory = apps.get_model("catalogue", "TempAdvatageCategory")

    temp_advatage_categories_by_old_pk = {
        temp_advatage_category.old_pk: temp_advatage_category
        for temp_advatage_category in TempAdvatageCategory.objects.all()
    }

    temp_advantages = []

    for advantage in Advantage.objects.all():
        temp_advatage_category = temp_advatage_categories_by_old_pk.get(
            advantage.advantage_category_id
        )

        if temp_advatage_category is None:
            raise ValueError(
                f"TempAdvatageCategory with old_pk={advantage.advantage_category_id} "
                f"was not found for Advantage pk={advantage.pk}."
            )

        temp_advantages.append(
            TempAdvantage(
                old_pk=advantage.pk,
                advantage_cs=advantage.advantage_cs,
                advantage_en=advantage.advantage_en,
                advantage_category=temp_advatage_category,
            )
        )

    TempAdvantage.objects.bulk_create(
        temp_advantages,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0039_tempadvantage_advantage_category"),
    ]

    operations = [
        migrations.RunPython(
            copy_advantages_to_temp,
            migrations.RunPython.noop,
        ),
    ]