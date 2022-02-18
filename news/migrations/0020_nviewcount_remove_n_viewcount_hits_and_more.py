# Generated by Django 4.0.1 on 2022-02-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_n_viewcount_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='NViewcount',
            fields=[
                ('v_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'N_Viewcount',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='n_viewcount',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='n_viewcount',
            name='id',
        ),
        migrations.RemoveField(
            model_name='n_viewcount',
            name='n',
        ),
        migrations.DeleteModel(
            name='Viewcount',
        ),
        migrations.DeleteModel(
            name='N_Viewcount',
        ),
    ]
