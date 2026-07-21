from django.db import migrations
from django.template.defaultfilters import slugify


def make_unique_slug(base_slug, used_slugs):
    slug = base_slug or "measure-group"
    unique_slug = slug
    counter = 2

    while unique_slug in used_slugs:
        unique_slug = f"{slug}-{counter}"
        counter += 1

    used_slugs.add(unique_slug)
    return unique_slug


def populate_measure_group_slugs(apps, schema_editor):
    MeasureGroup = apps.get_model("catalogue", "MeasureGroup")

    used_slugs_cs = set()
    used_slugs_en = set()

    for measure_group in MeasureGroup.objects.order_by("name_cs", "uuid"):
        if measure_group.slug_cs:
            used_slugs_cs.add(measure_group.slug_cs)

        if measure_group.slug_en:
            used_slugs_en.add(measure_group.slug_en)

    for measure_group in MeasureGroup.objects.order_by("name_cs", "uuid"):
        update_fields = []

        if not measure_group.slug_cs:
            measure_group.slug_cs = make_unique_slug(
                slugify(measure_group.name_cs),
                used_slugs_cs,
            )
            update_fields.append("slug_cs")

        if not measure_group.slug_en and measure_group.name_en:
            measure_group.slug_en = make_unique_slug(
                slugify(measure_group.name_en),
                used_slugs_en,
            )
            update_fields.append("slug_en")

        if update_fields:
            measure_group.save(update_fields=update_fields)


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0077_measuregroup_slug_cs_measuregroup_slug_en"),
    ]

    operations = [
        migrations.RunPython(
            populate_measure_group_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
    ]