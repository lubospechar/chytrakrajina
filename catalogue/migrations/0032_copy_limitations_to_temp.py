from django.db import migrations


def copy_limitations_to_temp(apps, schema_editor):
    Limitation = apps.get_model("catalogue", "Limitation")
    TempLimitation = apps.get_model("catalogue", "TempLimitation")

    temp_limitations = [
        TempLimitation(
            old_pk=limitation.pk,
            limitation_cs=limitation.limitation_cs,
            limitation_en=limitation.limitation_en,
        )
        for limitation in Limitation.objects.all()
    ]

    TempLimitation.objects.bulk_create(
        temp_limitations,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0031_templimitation"),
    ]

    operations = [
        migrations.RunPython(
            copy_limitations_to_temp,
            migrations.RunPython.noop,
        ),
    ]