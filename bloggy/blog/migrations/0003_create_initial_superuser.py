from django.db import migrations
from django.conf import settings
import os

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    username = os.environ.get('DJANGO_ADMIN_USERNAME')
    email = os.environ.get('DJANGO_ADMIN_EMAIL')
    password = os.environ.get('DJANGO_ADMIN_PASSWORD')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)

class Migration(migrations.Migration):

    dependencies = [
        # Specify dependencies if any
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop),
    ]
