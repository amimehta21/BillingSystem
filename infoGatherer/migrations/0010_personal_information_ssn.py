# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0009_remove_personal_information_ssn'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_information',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(default=b'', max_length=11),
        ),
    ]
