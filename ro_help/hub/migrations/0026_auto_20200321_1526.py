# Generated by Django 3.0.4 on 2020-03-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0025_registerngorequestvote"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registerngorequest",
            name="dsu_approved",
        ),
        migrations.RemoveField(
            model_name="registerngorequest",
            name="ffc_approved",
        ),
    ]
