# Generated by Django 3.0.3 on 2020-03-17 11:48

from django.db import migrations, models


def normalize_birthplace(apps, schema_editor):
    Usager = apps.get_model("aidants_connect_web", "Usager")
    for usager in Usager.objects.all():
        usager.normalize_birthplace()


class Migration(migrations.Migration):

    dependencies = [
        ("aidants_connect_web", "0018_add_journal_action_print_mandat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usager",
            name="birthcountry",
            field=models.CharField(default="99100", max_length=5),
        ),
        migrations.AlterField(
            model_name="usager",
            name="birthplace",
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name="usager",
            name="gender",
            field=models.CharField(
                choices=[("female", "Femme"), ("male", "Homme")],
                default="female",
                max_length=6,
            ),
        ),
        # Pad `birthplace` field with zeroes to ensure FranceConnect compliance
        migrations.RunPython(normalize_birthplace),
    ]