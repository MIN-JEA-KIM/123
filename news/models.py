# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class N_Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'N_category'


class N_CategoryDetail(models.Model):
    cd_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(N_Category, models.DO_NOTHING)
    cd_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'N_category_detail'


class News(models.Model):
    n_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Press', models.DO_NOTHING, blank=True, null=True)
    cd = models.ForeignKey(N_CategoryDetail, models.DO_NOTHING, blank=True, null=True)
    n_title = models.CharField(max_length=1024)
    nd_img = models.CharField(max_length=1024, blank=True, null=True)
    n_input = models.DateTimeField(blank=True, null=True)
    o_link = models.CharField(unique=True, max_length=768, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'News'

class N_content(models.Model):
    nc_id = models.AutoField(primary_key=True)
    n = models.ForeignKey('News', models.DO_NOTHING, blank=True, null=True)
    n_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_content'

class Viewcount(models.Model):
    hits = models.PositiveIntegerField(default=0, blank=True)
    n = models.ForeignKey(News, models.DO_NOTHING)
    user = models.ForeignKey('Memberinfo', models.DO_NOTHING, blank=True, null=True)

    def __unicode__(self):
        return self.hits

class N_summarization(models.Model):
    ns_id = models.AutoField(primary_key=True)
    n = models.ForeignKey('News', models.DO_NOTHING, blank=True, null=True)
    ns_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_summarization'

class Press(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'Press'

class N_content(models.Model):
    nc_id = models.AutoField(primary_key=True)
    n = models.ForeignKey('News', models.DO_NOTHING, blank=True, null=True)
    n_content = models.TextField(blank=True, null=True)
    hits = models.PositiveIntegerField(blank=True, default=0, verbose_name='조회수')
    recommend = models.PositiveIntegerField(default=0)

    @property
    def total_recommend(self):
        return self.recommend.count() #추천 갯수

    class Meta:
        managed = False
        db_table = 'N_content'

# 조회수 테이블

#2022-02-07 park-jong-won  add ScrollData,Log
class ScrollData(models.Model):
    ipaddr = models.CharField(max_length=15)
    acstime = models.DateTimeField(auto_now = True)
    url = models.CharField(db_column='URL', max_length=45)  # Field name made lowercase.
    staytime = models.IntegerField()
    scroll = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Scroll_Data'

class Log(models.Model):
    ipaddr = models.CharField(db_column='IPaddr', max_length=15, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase.
    acstime = models.DateTimeField(blank=True, null=True, auto_now = True)
    url = models.CharField(db_column='URL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Log'


class Memberinfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memberinfo'