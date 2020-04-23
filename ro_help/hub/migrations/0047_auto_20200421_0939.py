# Generated by Django 3.0.4 on 2020-04-21 09:39

from django.db import migrations, models
import hub.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0046_auto_20200414_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ngo',
            options={'ordering': ['name'], 'verbose_name': 'My organization', 'verbose_name_plural': 'My organizations'},
        ),
        migrations.AddField(
            model_name='registerngorequest',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='avatar',
            field=models.ImageField(max_length=300, storage=hub.storage_backends.PublicMediaStorage(), upload_to='', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='last_balance_sheet',
            field=models.FileField(blank=True, max_length=300, null=True, storage=hub.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='First page of last balance sheet'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='mobilpay_private_key',
            field=models.FileField(blank=True, max_length=300, null=True, storage=hub.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='Mobilpay Private key'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='mobilpay_public_key',
            field=models.FileField(blank=True, max_length=300, null=True, storage=hub.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='Mobilpay Public key'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='statute',
            field=models.FileField(blank=True, max_length=300, null=True, storage=hub.storage_backends.PrivateMediaStorage(), upload_to='', verbose_name='NGO Statute'),
        ),
    ]