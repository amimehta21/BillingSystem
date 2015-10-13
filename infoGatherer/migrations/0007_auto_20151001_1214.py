# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0006_personal_information_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_information',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(max_length=11),
        ),
    ]
