# Generated by Django 4.1.5 on 2023-01-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('wallet_export', models.CharField(help_text="lndhub wallet export, e.g 'lndhub://USERNAME:PASSWORD@https://lndhub.io'", max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.wallet'),
        ),
    ]