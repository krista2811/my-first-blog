# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_approved_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
    ]
