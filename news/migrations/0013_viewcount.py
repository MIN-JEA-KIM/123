# Generated by Django 4.0.1 on 2022-02-17 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_delete_viewcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hits', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='조회수')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.memberinfo')),
            ],
        ),
    ]
