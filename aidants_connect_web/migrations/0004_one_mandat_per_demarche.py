# Generated by Django 2.2.4 on 2019-08-30 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("aidants_connect_web", "0003_auto_20190827_1432")]

    operations = [
        migrations.AddField(
            model_name="journal",
            name="mandat",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="connection",
            name="mandat",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="aidants_connect_web.Mandat",
            ),
        ),
        migrations.RemoveField(model_name="mandat", name="perimeter"),
        migrations.AddField(
            model_name="mandat",
            name="demarche",
            field=models.CharField(default="No démarche", max_length=100),
            preserve_default=False,
        ),
    ]
