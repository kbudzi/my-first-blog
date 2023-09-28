# Generated by Django 4.1.6 on 2023-09-25 13:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import offerweb.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indeksy',
            name='Oferta',
        ),
        migrations.AddField(
            model_name='indeksy',
            name='kontrahent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offerweb.kontrahent'),
        ),
        migrations.AddField(
            model_name='kontrahent',
            name='miejscowosc',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='kontrahent',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+48 ', max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='kontrahent',
            name='ulica',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='oferty',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oferty',
            name='order',
            field=offerweb.fields.OrderField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(1, 'w trakcie'), (0, 'nowa'), (3, 'wysłana'), (2, 'opracowana')], default=0),
        ),
        migrations.AddField(
            model_name='technologia',
            name='indeks',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offerweb.indeksy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologia',
            name='tj',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='technologia',
            name='tpz',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='czy_mat',
            field=models.PositiveBigIntegerField(choices=[(1, 'Nie'), (0, 'Tak')], default=1),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='ilosc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='indeksy',
            name='indeks',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='kontrahent',
            name='Nazwa',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='kontrahent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='oferty',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='operacje',
            name='typ_operacji',
            field=models.PositiveBigIntegerField(choices=[(1, 'Kooperacja'), (0, 'Zwykła')], default=0),
        ),
        migrations.AlterField(
            model_name='technologia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='technologia',
            name='operacja',
        ),
        migrations.AddField(
            model_name='indeksy',
            name='oferta',
            field=models.ManyToManyField(related_name='oferty', to='offerweb.oferty'),
        ),
        migrations.AddField(
            model_name='technologia',
            name='operacja',
            field=models.ManyToManyField(related_name='technologie', to='offerweb.operacje'),
        ),
    ]
