# Generated by Django 3.2.20 on 2023-09-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SunSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('photos', models.TextField(max_length=100)),
                ('review_score', models.TextField(max_length=20, null=True)),
                ('hours', models.TextField(max_length=150, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
                ('tips', models.TextField(max_length=3000, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sun_set', to='app.city')),
            ],
        ),
    ]
