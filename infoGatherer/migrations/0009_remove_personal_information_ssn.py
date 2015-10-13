# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0008_auto_20151001_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_information',
            name='ssn',
        ),
    ]
