# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('infoGatherer', '0015_personal_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance_Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'Primary', max_length=10, choices=[(b'Primary', b'Primary'), (b'Secondary', b'Secondary'), (b'Tertiary', b'Tertiary')])),
                ('status', models.CharField(default=b'Active', max_length=10, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive'), (b'Invalid', b'Invalid'), (b'Not Found', b'Not Found')])),
                ('insurance_id', models.CharField(default=b'', max_length=32)),
                ('patient', models.ForeignKey(to='infoGatherer.Personal_Information')),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('code', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=256)),
                ('address', models.CharField(default=b'', max_length=256)),
                ('city', models.CharField(default=b'', max_length=128)),
                ('state', localflavor.us.models.USStateField(default=b'', max_length=2, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('zip', models.IntegerField(default=b'')),
                ('phone', localflavor.us.models.PhoneNumberField(default=b'XXX-XXX-XXXX', max_length=20, null=True, blank=True)),
                ('type', models.CharField(default=b'Active', max_length=1, choices=[(b'M', b'Medicare'), (b'C', b'Commercial')])),
            ],
        ),
        migrations.AddField(
            model_name='insurance_information',
            name='payer',
            field=models.ForeignKey(to='infoGatherer.Payer'),
        ),
    ]
