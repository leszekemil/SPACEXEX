# Generated by Django 3.1.2 on 2020-10-20 14:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(choices=[('Kennedy Space Center / USA', 'Kennedy Space Center / USA'), ('Boca Chica / USA', 'Boca Chica / USA'), ('Baikonur CosmodromE / RUSSIA', 'Baikonur CosmodromE / RUSSIA'), ('Vostochny Cosmodrome / RUSSIA', 'Vostochny Cosmodrome / RUSSIA'), ('Wenchang Satellite Launch Center / CHINA', 'Wenchang Satellite Launch Center / CHINA'), ('Łeba-Rąbka / POLAND', 'Łeba-Rąbka / POLAND')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceOnOrbit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orbit', models.CharField(choices=[('LEO', 'LooEO'), ('MEO', 'MooEO'), ('GEO', 'GEO'), ('MEO', 'MEO'), ('MOON', 'MOON')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('weight', models.IntegerField(default=23000)),
                ('description', models.CharField(max_length=300)),
                ('destination_orbit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='satellie_orbit', to='space_app.placeonorbit')),
            ],
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('launch_price', models.IntegerField(default=78)),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='space_app.producer')),
            ],
        ),
        migrations.CreateModel(
            name='LaunchSiteRockets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('rocket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_app.rocket')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_app.launchsite')),
            ],
        ),
        migrations.AddField(
            model_name='launchsite',
            name='rockets',
            field=models.ManyToManyField(through='space_app.LaunchSiteRockets', to='space_app.Rocket'),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('departure_date', models.DateTimeField(auto_now_add=True)),
                ('launchsite', models.CharField(choices=[('Kennedy Space Center / USA', 'Kennedy Space Center / USA'), ('Boca Chica / USA', 'Boca Chica / USA'), ('Baikonur CosmodromE / RUSSIA', 'Baikonur CosmodromE / RUSSIA'), ('Vostochny Cosmodrome / RUSSIA', 'Vostochny Cosmodrome / RUSSIA'), ('Wenchang Satellite Launch Center / CHINA', 'Wenchang Satellite Launch Center / CHINA'), ('Łeba-Rąbka / POLAND', 'Łeba-Rąbka / POLAND')], max_length=40)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_app.placeonorbit')),
                ('rocket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_app.rocket')),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='space_app.satellite')),
            ],
        ),
    ]
