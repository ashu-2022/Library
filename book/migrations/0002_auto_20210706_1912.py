# Generated by Django 3.0.7 on 2021-07-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='book_pics'),
        ),
    ]
