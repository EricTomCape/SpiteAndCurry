# Generated by Django 3.1.2 on 2020-11-01 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20201031_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgfile',
            name='name',
            field=models.CharField(default='etc', max_length=200),
            preserve_default=False,
        ),
    ]