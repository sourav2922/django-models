# Generated by Django 4.0.7 on 2023-04-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=10)),
                ('salary', models.FloatField(max_length=100)),
                ('w_hrs', models.FloatField(max_length=50)),
            ],
        ),
    ]
