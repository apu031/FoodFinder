# Generated by Django 3.0.7 on 2020-06-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DropDownModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cities', models.CharField(choices=[('Toronto', 'Toronto')], default='green', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ParsedData',
            fields=[
                ('business_id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('stars', models.TextField(blank=True, null=True)),
                ('review_count', models.TextField(blank=True, null=True)),
                ('categories', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
