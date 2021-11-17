# Generated by Django 3.2.7 on 2021-11-10 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0003_auto_20211104_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='bioterio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Pesquisador.bioterio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_avaliador',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
