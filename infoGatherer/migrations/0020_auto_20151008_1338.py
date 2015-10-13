# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0019_auto_20151008_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payer',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(help_text=b'XXX-XXX-XXXX', max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='cell_phone',
            field=localflavor.us.models.PhoneNumberField(help_text=b'XXX-XXX-XXXX', max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='ssn',
            field=localflavor.us.models.USSocialSecurityNumberField(help_text=b'XXX-XX-XXXX', max_length=11, null=True, blank=True),
        ),
    ]
