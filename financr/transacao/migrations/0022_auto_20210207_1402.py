# Generated by Django 3.1.5 on 2021-02-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0021_auto_20210207_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='regularidade',
            field=models.IntegerField(blank=True, choices=[(1, 'Diário'), (2, 'Semanal'), (3, 'Mensal')], default=0),
        ),
    ]
