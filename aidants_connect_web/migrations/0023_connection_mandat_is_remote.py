# Generated by Django 3.0.4 on 2020-06-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aidants_connect_web", "0022_auto_20200515_1455"),
    ]

    operations = [
        migrations.AddField(
            model_name="connection",
            name="mandat_is_remote",
            field=models.BooleanField(default=False),
        ),
    ]
