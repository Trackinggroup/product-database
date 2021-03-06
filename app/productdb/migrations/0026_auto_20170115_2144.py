# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-15 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productdb', '0025_auto_20170109_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCheckInputChunks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveIntegerField()),
                ('input_product_ids_chunk', models.CharField(blank=True, max_length=65536)),
            ],
            options={
                'ordering': ['sequence'],
            },
        ),
        migrations.RemoveField(
            model_name='productcheck',
            name='input_product_ids',
        ),
        migrations.AddField(
            model_name='productcheckinputchunks',
            name='product_check',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productdb.ProductCheck'),
        ),
    ]
