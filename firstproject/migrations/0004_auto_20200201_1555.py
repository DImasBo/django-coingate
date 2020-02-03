# Generated by Django 2.2 on 2020-02-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstproject', '0003_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_currency',
            field=models.CharField(blank=True, choices=[('EUR', 'EUR'), ('USD', 'USD'), ('CAD', 'CAD'), ('BTC', 'BTC'), ('ETH', 'ETH')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='receive_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='receive_currency',
            field=models.CharField(blank=True, choices=[('EUR', 'EUR'), ('USD', 'USD'), ('CAD', 'CAD'), ('BTC', 'BTC'), ('ETH', 'ETH')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='price_curenncy',
            field=models.CharField(blank=True, choices=[('EUR', 'EUR'), ('USD', 'USD'), ('CAD', 'CAD'), ('BTC', 'BTC'), ('ETH', 'ETH')], max_length=8, null=True),
        ),
    ]
