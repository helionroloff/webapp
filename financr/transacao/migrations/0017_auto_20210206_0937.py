# Generated by Django 3.1.5 on 2021-02-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0016_auto_20210206_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='regularidade',
            field=models.IntegerField(choices=[(1, 'Diário'), (2, 'Semanal'), (3, 'Mensal'), (4, 'Pontual')], default=4),
        ),
    ]
