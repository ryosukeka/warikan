# Generated by Django 2.2.12 on 2020-04-18 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repayer', models.TextField()),
                ('reciever', models.TextField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tracs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.TextField()),
                ('nonpayer', models.TextField()),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.TextField()),
            ],
        ),
    ]