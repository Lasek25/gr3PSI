# Generated by Django 3.0.2 on 2020-01-30 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Schronisko', '0010_remove_zwierze_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='zwierze',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zwierze', to=settings.AUTH_USER_MODEL),
        ),
    ]
