from django.db import migrations


def copy_measure_groups_to_temp(apps, schema_editor):
    MeasureGroup = apps.get_model("catalogue", "MeasureGroup")
    TempMesureGroup = apps.get_model("catalogue", "TempMesureGroup")

    temp_measure_groups = [
        TempMesureGroup(
            old_pk=measure_group.pk,
            name_cs=measure_group.name_cs,
            name_en=measure_group.name_en,
            description_cs=measure_group.description_cs,
            description_en=measure_group.description_en,
            icon=measure_group.icon,
        )
        for measure_group in MeasureGroup.objects.all()
    ]

    TempMesureGroup.objects.bulk_create(
        temp_measure_groups,
        ignore_conflicts=True,
    )


def remove_copied_measure_groups_from_temp(apps, schema_editor):
    TempMesureGroup = apps.get_model("catalogue", "TempMesureGroup")
    TempMesureGroup.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0027_tempmesuregroup"),
    ]

    operations = [
        migrations.RunPython(
            copy_measure_groups_to_temp,
            remove_copied_measure_groups_from_temp,
        ),
    ]