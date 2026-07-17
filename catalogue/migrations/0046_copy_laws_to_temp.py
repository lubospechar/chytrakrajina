from django.db import migrations


def copy_laws_to_temp(apps, schema_editor):
    Law = apps.get_model("catalogue", "Law")
    TempLaw = apps.get_model("catalogue", "TempLaw")

    temp_laws = [
        TempLaw(
            old_pk=law.pk,
            description=law.description,
            url=law.url,
        )
        for law in Law.objects.all()
    ]

    TempLaw.objects.bulk_create(
        temp_laws,
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0045_templaw"),
    ]

    operations = [
        migrations.RunPython(
            copy_laws_to_temp,
            migrations.RunPython.noop,
        ),
    ]