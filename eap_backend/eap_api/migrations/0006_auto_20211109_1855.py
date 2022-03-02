# Generated by Django 3.2.8 on 2021-11-09 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eap_api', '0005_auto_20211109_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='argument',
            old_name='property_claim_id',
            new_name='property_claim',
        ),
        migrations.RenameField(
            model_name='context',
            old_name='goal_id',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='evidence',
            old_name='evidential_claim_id',
            new_name='evidential_claim',
        ),
        migrations.RenameField(
            model_name='evidentialclaim',
            old_name='argument_id',
            new_name='argument',
        ),
        migrations.RenameField(
            model_name='propertyclaim',
            old_name='goal_id',
            new_name='goal',
        ),
        migrations.RenameField(
            model_name='systemdescription',
            old_name='goal_id',
            new_name='goal',
        ),
    ]