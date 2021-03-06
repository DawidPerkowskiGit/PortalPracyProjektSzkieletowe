# Generated by Django 2.2.7 on 2021-04-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_fieldofstudy'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdpowiedzNaOgloszenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=30)),
                ('rodzaj_wyksztalcenia', models.CharField(max_length=30)),
                ('staz', models.CharField(max_length=30)),
                ('dodatkowe_informacje', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ogloszenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('stanowisko', models.CharField(max_length=30)),
                ('staz', models.CharField(max_length=30)),
                ('branza', models.CharField(max_length=30)),
                ('zawod', models.CharField(max_length=30)),
                ('do_kiedy_aktualna', models.DateField()),
                ('praca_zdalna', models.BooleanField()),
                ('dodatkowe_wymagania', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Przedsiebiorstwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('adres', models.CharField(max_length=100)),
                ('opis', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='FieldOfStudy',
        ),
        migrations.RemoveField(
            model_name='student',
            name='faculty',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='ogloszenie',
            name='przedsiebiorstwo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Przedsiebiorstwo'),
        ),
        migrations.AddField(
            model_name='odpowiedznaogloszenie',
            name='ogloszenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Ogloszenie'),
        ),
    ]
