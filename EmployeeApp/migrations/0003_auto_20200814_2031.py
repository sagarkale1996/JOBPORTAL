# Generated by Django 3.1 on 2020-08-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0002_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='eid',
            field=models.IntegerField(default=0, max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
