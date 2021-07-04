# Generated by Django 2.1.5 on 2019-07-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullSite', '0009_contect_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='State',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='accountNo',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='account',
            name='totalOrder',
            field=models.IntegerField(default=0),
        ),
    ]
