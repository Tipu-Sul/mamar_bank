# Generated by Django 4.2.7 on 2024-01-01 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_remove_transactions_is_bankrupt'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankRupt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bankrupt', models.BooleanField(default=False)),
            ],
        ),
    ]
