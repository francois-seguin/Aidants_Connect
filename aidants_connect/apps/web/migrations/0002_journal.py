# Generated by Django 2.2.4 on 2019-08-26 15:18

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("web", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Journal",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("connect_aidant", "Connexion d'un aidant"),
                            ("create_mandat", "Création d'un mandat"),
                            ("use_mandat", "Utilisation d'un mandat"),
                        ],
                        max_length=30,
                    ),
                ),
                ("initiator", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "demarches",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ("usager", models.TextField(blank=True, null=True)),
                ("duree", models.IntegerField(blank=True, null=True)),
                ("access_token", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="connection",
            name="aidant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
