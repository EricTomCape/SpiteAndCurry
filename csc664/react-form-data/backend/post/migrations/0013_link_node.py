# Generated by Django 3.1.2 on 2020-12-08 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20201207_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.imgfile')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_image', to='post.imgfile')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_image', to='post.imgfile')),
            ],
        ),
    ]
