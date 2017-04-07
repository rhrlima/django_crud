# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('tarefa_id', models.AutoField(serialize=False, primary_key=True)),
                ('tarefa_nome', models.CharField(max_length=120)),
                ('tarefa_data_inicio', models.DateField()),
                ('tarefa_concluido', models.BooleanField(verbose_name=b'Concluido')),
            ],
        ),
    ]
