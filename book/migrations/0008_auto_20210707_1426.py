# Generated by Django 3.0.7 on 2021-07-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20210707_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[(0, 'CS'), (1, 'Non-CS'), (2, 'Common')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.IntegerField(choices=[('English', 'English'), ('Hindi', 'Hindi'), ('German', 'German'), ('English(U.S.)', 'English(U.S.)'), ('English(India)', 'English(India)')], null=True),
        ),
    ]