# Generated by Django 4.1.6 on 2023-07-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerweb', '0018_alter_indeksy_czy_mat_alter_oferty_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indeksy',
            old_name='Oferta',
            new_name='oferta',
        ),
        migrations.AlterField(
            model_name='oferty',
            name='status',
            field=models.PositiveBigIntegerField(choices=[(2, 'opracowana'), (1, 'w trakcie'), (3, 'wysłana'), (0, 'nowa')], default=0),
        ),
        migrations.RemoveField(
            model_name='technologia',
            name='operacja',
        ),
        migrations.AddField(
            model_name='technologia',
            name='operacja',
            field=models.ManyToManyField(related_name='technologie', to='offerweb.operacje'),
        ),
    ]
