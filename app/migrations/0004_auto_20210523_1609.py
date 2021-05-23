# Generated by Django 2.2 on 2021-05-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210523_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
