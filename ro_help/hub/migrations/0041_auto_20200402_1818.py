# Generated by Django 3.0.4 on 2020-04-02 18:18

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0040_auto_20200331_0856"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ngo",
            name="avatar",
            field=models.ImageField(
                max_length=300,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="Avatar",
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="last_balance_sheet",
            field=models.FileField(
                blank=True,
                max_length=300,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="First page of last balance sheet",
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="mobilpay_private_key",
            field=models.FileField(
                blank=True,
                max_length=300,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="mobilpay Private key",
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="mobilpay_public_key",
            field=models.FileField(
                blank=True,
                max_length=300,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="mobilpay Public key",
            ),
        ),
        migrations.AlterField(
            model_name="ngo",
            name="statute",
            field=models.FileField(
                blank=True,
                max_length=300,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="NGO Statute",
            ),
        ),
        migrations.AlterField(
            model_name="registerngorequest",
            name="last_balance_sheet",
            field=models.FileField(
                max_length=300,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="First page of last balance sheet",
            ),
        ),
        migrations.AlterField(
            model_name="registerngorequest",
            name="statute",
            field=models.FileField(
                max_length=300,
                storage=django.core.files.storage.FileSystemStorage(),
                upload_to="",
                verbose_name="NGO Statute",
            ),
        ),
        migrations.AlterField(
            model_name="registerngorequestvote",
            name="motivation",
            field=models.TextField(
                blank=True, help_text="Motivate your decision", max_length=500, null=True, verbose_name="Motivation"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="registerngorequestvote",
            unique_together={("ngo_request", "entity")},
        ),
    ]
