# Generated by Django 3.1.2 on 2020-10-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_app', '0002_auto_20201022_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeonorbit',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
