# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.ManyToManyField(to='FirstApp.Ingredient')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('auto_increment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('mail', models.CharField(unique=True, max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(to='FirstApp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='recipes',
            field=models.ManyToManyField(to='FirstApp.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(to='FirstApp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(to='FirstApp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(to='FirstApp.Recipe'),
            preserve_default=True,
        ),
    ]
