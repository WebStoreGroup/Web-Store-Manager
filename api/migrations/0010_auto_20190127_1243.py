# Generated by Django 2.1.5 on 2019-01-27 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_itemrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemrating',
            old_name='rate',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rating',
        ),
    ]