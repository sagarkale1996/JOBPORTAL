# Generated by Django 3.1 on 2020-08-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sid', models.IntegerField()),
                ('Sname', models.CharField(max_length=20)),
                ('Saddr', models.CharField(max_length=50)),
                ('Sscholarship', models.FloatField()),
            ],
        ),
    ]
