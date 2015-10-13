# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0005_personal_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_information',
            name='city',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
