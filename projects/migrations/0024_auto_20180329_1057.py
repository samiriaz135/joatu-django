# Generated by Django 2.0.3 on 2018-03-29 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20180327_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_attendees',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='projects.Project'),
        ),
    ]
