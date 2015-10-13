import django
django.setup()
from django.db import connection

tables = connection.introspection.table_names()

for each in tables:
    print each