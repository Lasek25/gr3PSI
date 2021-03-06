# Generated by Django 2.2.7 on 2019-11-14 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strefa', models.CharField(choices=[('DO_ADOPCJI', 'do_adopcji'), ('RESOCJALIZACJA', 'resocjalizacja'), ('MLODE', 'młode')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('nazwisko', models.CharField(max_length=45)),
                ('pesel', models.CharField(max_length=11, unique=True)),
                ('telefon', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Typ_Umowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stanowisko', models.CharField(choices=[('OPIEKUN', 'opiekun'), ('WETERYNARZ', 'weterynarz'), ('ADMINISTRACJA', 'administracja'), ('PREZES', 'prezes')], max_length=13)),
                ('pensja', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zwierze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gatunek', models.CharField(choices=[('PIES', 'pies'), ('KOT', 'kot')], max_length=4)),
                ('imie', models.CharField(max_length=45)),
                ('rasa', models.CharField(default='mieszana', max_length=45)),
                ('plec', models.CharField(choices=[('SAMIEC', 'samiec'), ('SAMICA', 'samica')], max_length=45)),
                ('data_przyjecia', models.DateField()),
                ('boks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Schronisko.Boks')),
                ('pracownik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Schronisko.Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Umowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_zatrudnienia', models.DateField()),
                ('data_konca_umowy', models.DateField()),
                ('nr_konta', models.CharField(max_length=26)),
                ('typ_umowy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Schronisko.Typ_Umowy')),
            ],
        ),
        migrations.AddField(
            model_name='pracownik',
            name='umowa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Schronisko.Umowa'),
        ),
        migrations.AddField(
            model_name='boks',
            name='pracownik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Schronisko.Pracownik'),
        ),
    ]
