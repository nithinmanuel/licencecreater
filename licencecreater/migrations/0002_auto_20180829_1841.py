# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import licencecreater.models


class Migration(migrations.Migration):

    dependencies = [
        ('licencecreater', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='converted',
            field=models.FileField(default=None, upload_to=licencecreater.models.get_converted_document_path),
        ),
        migrations.AddField(
            model_name='document',
            name='uploaded',
            field=models.FileField(default=None, upload_to=licencecreater.models.get_uploaded_document_path),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='name',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
