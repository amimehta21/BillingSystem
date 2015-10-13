# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0011_auto_20151001_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_information',
            name='country',
            field=django_countries.fields.CountryField(default=b'us', max_length=2),
        ),
    ]
