# Generated by Django 2.2.7 on 2019-11-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custname', models.CharField(max_length=25)),
                ('custid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
