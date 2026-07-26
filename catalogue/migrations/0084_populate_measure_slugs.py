from django.db import migrations
from django.template.defaultfilters import slugify


def make_unique_slug(base_slug, used_slugs):
    slug = base_slug or "measure"
    unique_slug = slug
    counter = 2

    while unique_slug in used_slugs:
        unique_slug = f"{slug}-{counter}"
        counter += 1

    used_slugs.add(unique_slug)
    return unique_slug


def populate_measure_slugs(apps, schema_editor):
    Measure = apps.get_model("catalogue", "Measure")

    used_slugs_cs = set()
    used_slugs_en = set()

    for measure in Measure.objects.order_by("name_cs", "uuid"):
        if measure.slug_cs:
            used_slugs_cs.add(measure.slug_cs)

        if measure.slug_en:
            used_slugs_en.add(measure.slug_en)

    for measure in Measure.objects.order_by("name_cs", "uuid"):
        update_fields = []

        if not measure.slug_cs:
            measure.slug_cs = make_unique_slug(
                slugify(measure.name_cs),
                used_slugs_cs,
            )
            update_fields.append("slug_cs")

        if not measure.slug_en and measure.name_en:
            measure.slug_en = make_unique_slug(
                slugify(measure.name_en),
                used_slugs_en,
            )
            update_fields.append("slug_en")

        if update_fields:
            measure.save(update_fields=update_fields)


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0083_measure_slug_cs_measure_slug_en"),
    ]

    operations = [
        migrations.RunPython(
            populate_measure_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
    ]