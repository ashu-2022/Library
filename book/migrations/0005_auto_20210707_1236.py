# Generated by Django 3.0.7 on 2021-07-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210707_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.IntegerField(choices=[(0, 'CS'), (1, 'Non-CS'), (2, 'Common')], default=0, null=True),
        ),
    ]
