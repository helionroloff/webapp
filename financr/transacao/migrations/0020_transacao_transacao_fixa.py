# Generated by Django 3.1.5 on 2021-02-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0019_auto_20210206_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='transacao_fixa',
            field=models.BooleanField(default=0, max_length=1),
        ),
    ]