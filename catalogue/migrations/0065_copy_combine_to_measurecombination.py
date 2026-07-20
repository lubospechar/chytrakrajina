from django.db import migrations


def copy_combine_to_measurecombination(apps, schema_editor):
    Measure = apps.get_model("catalogue", "Measure")
    MeasureCombination = apps.get_model("catalogue", "MeasureCombination")

    for measure in Measure.objects.all():
        for related_measure in measure.combine.all():
            MeasureCombination.objects.get_or_create(
                from_measure=measure,
                to_measure=related_measure,
            )


def remove_measurecombination_data(apps, schema_editor):
    MeasureCombination = apps.get_model("catalogue", "MeasureCombination")
    MeasureCombination.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0064_measure_new_combine_alter_measure_combine"),
    ]

    operations = [
        migrations.RunPython(
            copy_combine_to_measurecombination,
            remove_measurecombination_data,
        ),
    ]