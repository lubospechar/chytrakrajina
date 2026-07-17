from django.db import migrations


def copy_location_types_to_temp(apps, schema_editor):
    LocationType = apps.get_model("catalogue", "LocationType")
    TempLocationType = apps.get_model("catalogue", "TempLocationType")

    temp_location_types = [
        TempLocationType(
            old_pk=location_type.pk,
            location_type_cs=location_type.location_type_cs,
            location_type_en=location_type.location_type_en,
        )
        for location_type in LocationType.objects.all()
    ]

    TempLocationType.objects.bulk_create(
        temp_location_types,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0029_templocationtype"),
    ]

    operations = [
        migrations.RunPython(
            copy_location_types_to_temp,
            migrations.RunPython.noop,
        ),
    ]