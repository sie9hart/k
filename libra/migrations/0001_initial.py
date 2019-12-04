# Generated by Django 2.2.7 on 2019-11-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=25)),
                ('isbn', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]