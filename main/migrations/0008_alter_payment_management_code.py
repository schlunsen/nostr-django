# Generated by Django 4.1.5 on 2023-01-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_payment_management_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='management_code',
            field=models.CharField(blank=True, default='yXPtbq', max_length=50, null=True),
        ),
    ]
