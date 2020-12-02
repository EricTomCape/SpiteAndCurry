# Generated by Django 3.1.2 on 2020-10-30 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20201029_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('facets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.facet')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.imgfile')),
            ],
        ),
    ]