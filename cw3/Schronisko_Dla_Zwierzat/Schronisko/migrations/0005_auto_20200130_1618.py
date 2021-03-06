# Generated by Django 3.0.2 on 2020-01-30 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Schronisko', '0004_auto_20200130_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boks',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='zwierze',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zwierzeta', to=settings.AUTH_USER_MODEL),
        ),
    ]
