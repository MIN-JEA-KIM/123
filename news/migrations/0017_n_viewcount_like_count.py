# Generated by Django 4.0.1 on 2022-02-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_n_viewcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='n_viewcount',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]