# Generated by Django 2.2 on 2020-02-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
