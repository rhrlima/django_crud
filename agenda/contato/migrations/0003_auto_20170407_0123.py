# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0002_tarefas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]
