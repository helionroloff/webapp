# Generated by Django 3.1.5 on 2021-02-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0020_transacao_transacao_fixa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='regularidade',
            field=models.IntegerField(blank=True, choices=[(1, 'Diário'), (2, 'Semanal'), (3, 'Mensal')], default=4),
        ),
    ]