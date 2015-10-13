# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0007_auto_20151001_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_information',
            name='middle_name',
            field=models.CharField(default=b'', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(default=b'', max_length=11),
        ),
    ]
