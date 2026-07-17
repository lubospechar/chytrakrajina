from django.db import migrations


def copy_sdgs_to_temp(apps, schema_editor):
    SDG = apps.get_model("catalogue", "SDG")
    TempSDG = apps.get_model("catalogue", "TempSDG")

    temp_sdgs = [
        TempSDG(
            old_pk=sdg.pk,
            sdg_number=sdg.sdg_number,
            sdg_name=sdg.sdg_name,
            icon=sdg.icon,
        )
        for sdg in SDG.objects.all()
    ]

    TempSDG.objects.bulk_create(
        temp_sdgs,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0043_tempsdg"),
    ]

    operations = [
        migrations.RunPython(
            copy_sdgs_to_temp,
            migrations.RunPython.noop,
        ),
    ]