# Generated by Django 2.2.3 on 2019-08-05 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aidants_connect_web', '0002_auto_20190801_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='usager',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]