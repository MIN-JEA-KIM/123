# Generated by Django 4.0.1 on 2022-02-09 16:07
# Generated by Django 4.0.1 on 2022-02-10 13:58


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_n_category_n_categorydetail_n_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.CharField(blank=True, db_collation='utf8_general_ci', db_column='IPaddr', max_length=15, null=True)),
                ('acstime', models.DateTimeField(auto_now=True, null=True)),
                ('url', models.CharField(blank=True, db_column='URL', max_length=45, null=True)),
            ],
            options={
                'db_table': 'Log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ScrollData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.CharField(max_length=15)),
                ('acstime', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(db_column='URL', max_length=45)),
                ('staytime', models.IntegerField()),
                ('scroll', models.IntegerField()),
            ],
            options={
                'db_table': 'Scroll_Data',
                'managed': False,
            },
        ),
    ]
