# Generated by Django 3.0.4 on 2020-03-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0029_ngoreportitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ngoreportitem",
            name="date",
            field=models.DateField(verbose_name="Date"),
        ),
    ]
