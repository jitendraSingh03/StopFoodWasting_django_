# Generated by Django 2.1.5 on 2019-07-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullSite', '0012_auto_20190702_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='response',
            field=models.CharField(default='None', max_length=300),
        ),
    ]