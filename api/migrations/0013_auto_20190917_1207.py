# Generated by Django 2.2.5 on 2019-09-17 12:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_token_enabled'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Token',
            new_name='ApiToken',
        ),
    ]
