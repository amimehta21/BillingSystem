# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0016_auto_20151008_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payer',
            name='type',
        ),
    ]
