# Generated by Django 3.1.4 on 2020-12-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionID', models.CharField(max_length=25, verbose_name='Идентификационный номер')),
                ('TransactionAmt', models.IntegerField()),
                ('Card1', models.IntegerField()),
                ('Card2', models.IntegerField()),
                ('Сard6', models.CharField(max_length=10, verbose_name='Тип карты')),
            ],
        ),
    ]