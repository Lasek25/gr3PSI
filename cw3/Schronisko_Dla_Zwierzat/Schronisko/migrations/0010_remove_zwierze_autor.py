# Generated by Django 3.0.2 on 2020-01-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schronisko', '0009_auto_20200130_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zwierze',
            name='autor',
        ),
    ]
