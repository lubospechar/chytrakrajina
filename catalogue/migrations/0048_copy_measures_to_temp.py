from django.db import migrations


def get_required(mapping, old_pk, target_model_name, source_relation_name, source_pk):
    item = mapping.get(old_pk)

    if item is None:
        raise ValueError(
            f"{target_model_name} with old_pk={old_pk} was not found "
            f"for {source_relation_name} on source pk={source_pk}."
        )

    return item


def copy_measures_to_temp(apps, schema_editor):
    Measure = apps.get_model("catalogue", "Measure")
    TempMeasure = apps.get_model("catalogue", "TempMeasure")
    TempMesureGroup = apps.get_model("catalogue", "TempMesureGroup")
    TempLocationType = apps.get_model("catalogue", "TempLocationType")
    TempAdvantage = apps.get_model("catalogue", "TempAdvantage")
    TempLimitation = apps.get_model("catalogue", "TempLimitation")
    TempSDG = apps.get_model("catalogue", "TempSDG")
    TempLaw = apps.get_model("catalogue", "TempLaw")

    temp_measure_groups_by_old_pk = {
        temp_measure_group.old_pk: temp_measure_group
        for temp_measure_group in TempMesureGroup.objects.all()
    }

    temp_location_types_by_old_pk = {
        temp_location_type.old_pk: temp_location_type
        for temp_location_type in TempLocationType.objects.all()
    }

    temp_advantages_by_old_pk = {
        temp_advantage.old_pk: temp_advantage
        for temp_advantage in TempAdvantage.objects.all()
    }

    temp_limitations_by_old_pk = {
        temp_limitation.old_pk: temp_limitation
        for temp_limitation in TempLimitation.objects.all()
    }

    temp_sdgs_by_old_pk = {
        temp_sdg.old_pk: temp_sdg
        for temp_sdg in TempSDG.objects.all()
    }

    temp_laws_by_old_pk = {
        temp_law.old_pk: temp_law
        for temp_law in TempLaw.objects.all()
    }

    for measure in Measure.objects.all():
        if TempMeasure.objects.filter(old_pk=measure.pk).exists():
            continue

        temp_measure_group = get_required(
            temp_measure_groups_by_old_pk,
            measure.group_id,
            "TempMesureGroup",
            "Measure.group",
            measure.pk,
        )

        TempMeasure.objects.create(
            old_pk=measure.pk,
            name_cs=measure.name_cs,
            name_en=measure.name_en,
            group=temp_measure_group,
            short_description_cs=measure.short_description_cs,
            short_description_en=measure.short_description_en,
            description_cs=measure.description_cs,
            description_en=measure.description_en,
            purpose=measure.purpose,
            temperature=measure.temperature,
            water=measure.water,
            biodiversity=measure.biodiversity,
            air=measure.air,
            aesthetics=measure.aesthetics,
            complexity_of_realization=measure.complexity_of_realization,
            budget_choices=measure.budget_choices,
            price=measure.price,
            units=measure.units,
            time_horizon=measure.time_horizon,
            measure_size=measure.measure_size,
            diy=measure.diy,
        )

    temp_measures_by_old_pk = {
        temp_measure.old_pk: temp_measure
        for temp_measure in TempMeasure.objects.all()
    }

    for measure in Measure.objects.all():
        temp_measure = get_required(
            temp_measures_by_old_pk,
            measure.pk,
            "TempMeasure",
            "Measure",
            measure.pk,
        )

        temp_measure.location_type.set([
            get_required(
                temp_location_types_by_old_pk,
                location_type.pk,
                "TempLocationType",
                "Measure.location_type",
                measure.pk,
            )
            for location_type in measure.location_type.all()
        ])

        temp_measure.main_advantage.set([
            get_required(
                temp_advantages_by_old_pk,
                main_advantage.pk,
                "TempAdvantage",
                "Measure.main_advantage",
                measure.pk,
            )
            for main_advantage in measure.main_advantage.all()
        ])

        temp_measure.advantage.set([
            get_required(
                temp_advantages_by_old_pk,
                advantage.pk,
                "TempAdvantage",
                "Measure.advantage",
                measure.pk,
            )
            for advantage in measure.advantage.all()
        ])

        temp_measure.limitation.set([
            get_required(
                temp_limitations_by_old_pk,
                limitation.pk,
                "TempLimitation",
                "Measure.limitation",
                measure.pk,
            )
            for limitation in measure.limitation.all()
        ])

        temp_measure.sdg.set([
            get_required(
                temp_sdgs_by_old_pk,
                sdg.pk,
                "TempSDG",
                "Measure.sdg",
                measure.pk,
            )
            for sdg in measure.sdg.all()
        ])

        temp_measure.law.set([
            get_required(
                temp_laws_by_old_pk,
                law.pk,
                "TempLaw",
                "Measure.law",
                measure.pk,
            )
            for law in measure.law.all()
        ])

    for measure in Measure.objects.all():
        temp_measure = get_required(
            temp_measures_by_old_pk,
            measure.pk,
            "TempMeasure",
            "Measure",
            measure.pk,
        )

        temp_measure.combine.set([
            get_required(
                temp_measures_by_old_pk,
                combined_measure.pk,
                "TempMeasure",
                "Measure.combine",
                measure.pk,
            )
            for combined_measure in measure.combine.all()
        ])


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0047_tempmeasure"),
    ]

    operations = [
        migrations.RunPython(
            copy_measures_to_temp,
            migrations.RunPython.noop,
        ),
    ]