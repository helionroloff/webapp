# Generated by Django 3.1.5 on 2021-02-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0018_auto_20210206_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='transacao_efetivada',
            field=models.BooleanField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='regularidade',
            field=models.IntegerField(blank=True, choices=[(1, 'Diário'), (2, 'Semanal'), (3, 'Mensal'), (4, ' ')], default=4),
        ),
    ]
