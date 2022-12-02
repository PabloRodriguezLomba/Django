# Generated by Django 4.1.2 on 2022-10-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=150)),
                ('alta', models.DateTimeField(verbose_name='Fecha Alta')),
            ],
        ),
    ]