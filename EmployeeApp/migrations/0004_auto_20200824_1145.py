# Generated by Django 3.1 on 2020-08-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0003_auto_20200814_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
