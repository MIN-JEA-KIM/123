# Generated by Django 4.0.1 on 2022-02-21 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_n_viewcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='N_Viewcount',
        ),
    ]
