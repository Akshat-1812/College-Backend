# Generated by Django 3.1.5 on 2021-04-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210415_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='idCard',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='idcardstring',
            field=models.TextField(blank=True, null=True),
        ),
    ]
