# Generated by Django 2.0.3 on 2018-06-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0039_auto_20180618_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='oth_sub_cat',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='oth_category',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
