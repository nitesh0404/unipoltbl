# Generated by Django 2.2.3 on 2019-09-21 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model_rest', '0004_delete_operational_parameter_dummy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='operational_parameters',
            new_name='operational_parameter',
        ),
        migrations.AlterModelTable(
            name='operational_parameter',
            table='operationalparameter',
        ),
    ]