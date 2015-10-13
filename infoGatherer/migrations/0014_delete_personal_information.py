# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0013_auto_20151001_1247'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal_Information',
        ),
    ]
