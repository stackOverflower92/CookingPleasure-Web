# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_auto_20150907_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'FirstApp/photo/', blank=True),
            preserve_default=True,
        ),
    ]
