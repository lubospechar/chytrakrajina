from django.db import migrations


def copy_performances_to_temp(apps, schema_editor):
    Performance = apps.get_model("catalogue", "Performance")
    TempPerformance = apps.get_model("catalogue", "TempPerformance")
    TempMeasure = apps.get_model("catalogue", "TempMeasure")

    temp_measures_by_old_pk = {
        temp_measure.old_pk: temp_measure
        for temp_measure in TempMeasure.objects.all()
    }

    for performance in Performance.objects.all():
        if TempPerformance.objects.filter(old_pk=performance.pk).exists():
            continue

        temp_measure = temp_measures_by_old_pk.get(performance.measure_id)

        if temp_measure is None:
            raise ValueError(
                f"TempMeasure with old_pk={performance.measure_id} "
                f"was not found for Performance pk={performance.pk}."
            )

        TempPerformance.objects.create(
            old_pk=performance.pk,
            measure=temp_measure,
            performance=performance.performance,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0049_tempperformance"),
    ]

    operations = [
        migrations.RunPython(
            copy_performances_to_temp,
            migrations.RunPython.noop,
        ),
    ]