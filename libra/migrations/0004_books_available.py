# Generated by Django 2.2.7 on 2019-12-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0003_borrow1'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='available',
            field=models.IntegerField(default=0),
        ),
    ]
