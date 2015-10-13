# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0003_personal_information'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal_Information',
        ),
    ]
