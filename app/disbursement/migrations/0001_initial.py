# Generated by Django 3.0.7 on 2020-12-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_code', models.CharField(blank=True, max_length=500, null=True)),
                ('account_number', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=25)),
                ('remark', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.NullBooleanField(default=None)),
            ],
        ),
    ]
