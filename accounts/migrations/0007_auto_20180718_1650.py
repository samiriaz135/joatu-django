# Generated by Django 2.0.3 on 2018-07-18 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_olderthansixteen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservalidation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='olderThanSixteen',
        ),
        migrations.DeleteModel(
            name='userValidation',
        ),
    ]
