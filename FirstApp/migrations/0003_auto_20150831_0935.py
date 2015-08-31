# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_auto_20150831_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='auto_increment_id',
            new_name='List_id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='auto_increment_id',
            new_name='Menu_id',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='auto_increment_id',
            new_name='Recipe_id',
        ),
    ]
