# Generated by Django 2.2 on 2019-06-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidants_connect_web', '0002_connection_redirecturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demarche',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
