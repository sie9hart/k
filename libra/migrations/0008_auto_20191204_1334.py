# Generated by Django 2.2.7 on 2019-12-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0007_auto_20191204_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow1',
            name='custid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='borrow1',
            name='isbn',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
