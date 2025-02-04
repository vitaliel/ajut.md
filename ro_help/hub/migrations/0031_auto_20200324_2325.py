# Generated by Django 3.0.4 on 2020-03-24 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0030_auto_20200322_1540"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pendingregisterngorequest",
            options={"verbose_name": "NGO pending request", "verbose_name_plural": "NGO pending requests"},
        ),
        migrations.AlterModelOptions(
            name="registerngorequest",
            options={"verbose_name": "NGO register request", "verbose_name_plural": "NGO register requests"},
        ),
        migrations.AlterModelOptions(
            name="registerngorequestvote",
            options={
                "verbose_name": "NGO Register requests vote",
                "verbose_name_plural": "NGO Register requests votes",
            },
        ),
        migrations.AlterModelOptions(
            name="resourcetag",
            options={"verbose_name": "Resource tag", "verbose_name_plural": "Resource tags"},
        ),
    ]
