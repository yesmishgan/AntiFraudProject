# Generated by Django 3.1.4 on 2020-12-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fraud_monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Card1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='Card2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='TransactionAmt',
            field=models.FloatField(),
        ),
    ]
