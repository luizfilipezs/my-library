# Generated by Django 3.2.5 on 2021-07-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_lending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lending',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
    ]
