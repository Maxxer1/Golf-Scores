# Generated by Django 2.1 on 2019-04-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='to_par',
            field=models.IntegerField(editable=False),
        ),
    ]
