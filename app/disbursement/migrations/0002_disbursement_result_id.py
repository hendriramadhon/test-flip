# Generated by Django 3.0.7 on 2020-12-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disbursement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disbursement',
            name='result_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
