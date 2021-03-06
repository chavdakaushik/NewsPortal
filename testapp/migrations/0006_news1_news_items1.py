# Generated by Django 2.1.7 on 2019-05-25 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='news1',
            fields=[
                ('n_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='news_items1',
            fields=[
                ('ni_id', models.AutoField(primary_key=True, serialize=False)),
                ('des', models.CharField(max_length=64)),
                ('reporter_name', models.CharField(max_length=64)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.news1')),
            ],
        ),
    ]
