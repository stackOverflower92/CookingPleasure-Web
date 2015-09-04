# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0005_auto_20150903_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'../../photo', blank=True),
            preserve_default=True,
        ),
    ]
