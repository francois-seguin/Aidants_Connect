# Generated by Django 3.0.5 on 2020-05-28 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0025_rename_mandat_step1_prepare_fk"),
    ]

    operations = [
        migrations.RenameModel(old_name="Mandat", new_name="Autorisation"),
        migrations.RenameField(
            model_name="connection", old_name="mandat", new_name="autorisation",
        ),
        migrations.AlterField(
            model_name="connection",
            name="access_token",
            field=models.TextField(default="No token provided"),
        ),
        migrations.RenameField(
            model_name="journal", old_name="mandat", new_name="autorisation",
        ),
        migrations.AlterField(
            model_name="journal",
            name="action",
            field=models.CharField(
                choices=[
                    ("connect_aidant", "Connexion d'un aidant"),
                    ("activity_check_aidant", "Reprise de connexion d'un aidant"),
                    ("franceconnect_usager", "FranceConnexion d'un usager"),
                    ("update_email_usager", "L'email de l'usager a été modifié"),
                    ("create_attestation", "Création d'une attestation"),
                    ("create_autorisation", "Création d'une autorisation"),
                    ("use_autorisation", "Utilisation d'une autorisation"),
                    ("update_autorisation", "Renouvellement d'une autorisation"),
                    ("cancel_autorisation", "Révocation d'une autorisation"),
                ],
                max_length=30,
            ),
        ),
    ]
