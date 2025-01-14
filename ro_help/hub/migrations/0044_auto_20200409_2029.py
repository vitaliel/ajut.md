# Generated by Django 3.0.4 on 2020-04-09 20:29

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0043_auto_20200404_0914"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ngo",
            options={"verbose_name": "My organization", "verbose_name_plural": "My organizations"},
        ),
        migrations.AlterModelOptions(
            name="ngoneed",
            options={"ordering": ["-urgency"], "verbose_name": "Manage need", "verbose_name_plural": "Manage needs"},
        ),
        migrations.AlterModelOptions(
            name="ngoreportitem",
            options={"verbose_name": "Reports", "verbose_name_plural": "Reporta"},
        ),
        migrations.AlterModelOptions(
            name="pendingregisterngorequest",
            options={"verbose_name": "Pending NGO", "verbose_name_plural": "Pending NGOs"},
        ),
        migrations.AlterModelOptions(
            name="registerngorequest",
            options={"verbose_name": "Vote history", "verbose_name_plural": "Votes history"},
        ),
        migrations.AlterModelOptions(
            name="registerngorequestvote",
            options={"verbose_name": "My vote", "verbose_name_plural": "My votes"},
        ),
        migrations.AlterField(
            model_name="ngo",
            name="avatar",
            field=models.ImageField(
                max_length=300, storage=django.core.files.storage.FileSystemStorage(), upload_to="", verbose_name="Logo"
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="donations_description",
            field=models.TextField(blank=True, null=True, verbose_name="Donations description"),
        ),
    ]
