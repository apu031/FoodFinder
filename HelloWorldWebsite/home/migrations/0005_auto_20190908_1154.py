# Generated by Django 2.2.5 on 2019-09-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190908_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dropdownmodel',
            name='cities',
            field=models.CharField(choices=[('Toronto', 'Toronto'), ('Edmonton', 'Edmonton'), ('New york', 'New york'), ('Montreal', 'Montreal'), ('Ottawa', 'Ottawa')], default='green', max_length=6),
        ),
    ]
