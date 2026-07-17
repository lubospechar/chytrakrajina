from django.db import migrations


def copy_predesigns_to_temp(apps, schema_editor):
    PreDesign = apps.get_model("catalogue", "PreDesign")
    TempPreDesign = apps.get_model("catalogue", "TempPreDesign")

    temp_predesigns = [
        TempPreDesign(
            old_pk=predesign.pk,
            prereqisite=predesign.prereqisite,
        )
        for predesign in PreDesign.objects.all()
    ]

    TempPreDesign.objects.bulk_create(
        temp_predesigns,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0041_temppredesign"),
    ]

    operations = [
        migrations.RunPython(
            copy_predesigns_to_temp,
            migrations.RunPython.noop,
        ),
    ]