# Generated by Django 3.2.5 on 2021-11-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.TextField(max_length=1000),
        ),
    ]
