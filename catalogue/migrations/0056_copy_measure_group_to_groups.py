from django.db import migrations


def copy_measure_group_to_groups(apps, schema_editor):
    Measure = apps.get_model("catalogue", "Measure")

    for measure in Measure.objects.exclude(group_id__isnull=True):
        measure.groups.add(measure.group_id)


def remove_measure_group_from_groups(apps, schema_editor):
    Measure = apps.get_model("catalogue", "Measure")

    for measure in Measure.objects.exclude(group_id__isnull=True):
        measure.groups.remove(measure.group_id)


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0055_measure_groups"),
    ]

    operations = [
        migrations.RunPython(
            copy_measure_group_to_groups,
            remove_measure_group_from_groups,
        ),
    ]