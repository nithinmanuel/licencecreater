# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import licencecreater.models


class Migration(migrations.Migration):

    dependencies = [
        ('licencecreater', '0003_auto_20180829_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='converted',
            field=models.FileField(blank=True, null=True, default=None, upload_to=licencecreater.models.get_converted_document_path),
        ),
    ]
