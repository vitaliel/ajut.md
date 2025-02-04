# Generated by Django 3.0.4 on 2020-03-21 00:44

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hub", "0020_auto_20200320_2353"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentOrder",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                (
                    "order_id",
                    models.CharField(
                        blank=True, default=uuid.uuid4, max_length=100, unique=True, verbose_name="Order ID"
                    ),
                ),
                ("first_name", models.CharField(max_length=254, verbose_name="First name")),
                ("last_name", models.CharField(max_length=254, verbose_name="Lasts name")),
                ("phone", models.CharField(max_length=30, verbose_name="Phone")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("address", models.CharField(max_length=254, verbose_name="Address")),
                ("details", models.TextField(verbose_name="Details")),
                ("amount", models.FloatField(verbose_name="Amount")),
                (
                    "ngo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payment_orders",
                        to="hub.NGO",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment Order",
                "verbose_name_plural": "Payment Orders",
            },
        ),
        migrations.CreateModel(
            name="PaymentResponse",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name="modified"),
                ),
                ("r", models.TextField()),
                (
                    "payment_order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="responses",
                        to="mobilpay.PaymentOrder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Payment Order",
                "verbose_name_plural": "Payment Orders",
            },
        ),
    ]
