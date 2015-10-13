# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0017_remove_payer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='payer',
            name='type',
            field=models.CharField(default=b'C', max_length=1, choices=[(b'M', b'Medicare'), (b'C', b'Commercial')]),
        ),
    ]
