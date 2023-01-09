from django.db import models
from lndhub import Wallet as LNDHubWallet
from datetime import datetime


class Nip05User(models.Model):
    name = models.CharField(max_length=100)
    pub_key = models.CharField(max_length=300)
    relays = models.ManyToManyField("Relay", blank=True)

    def __str__(self):
        return self.name


class Relay(models.Model):
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name = models.CharField(max_length=300)
    wallet_export = models.CharField(
        max_length=250, help_text="lndhub wallet export, e.g 'lndhub://USERNAME:PASSWORD@https://lndhub.io'")

    def __str__(self):
        return self.name

def generate_management_code():
    from django.contrib.auth.models import User
    return User.objects.make_random_password(length=6)

class Payment(models.Model):
    username = models.CharField(max_length=100)
    lnurl = models.CharField(max_length=500, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    management_code = models.CharField(blank=True, null=True, default=generate_management_code(), max_length=50)
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, blank=True, null=True)

    def generate_invoice(self, amount=5000):
        wallet = LNDHubWallet(self.wallet.wallet_export)

        invoice = wallet.create_invoice(
            amount=amount, description='Bekindorrewind donation')
        self.lnurl = invoice['pay_req']
        self.save()

    def confirm_payment(self):
        wallet = Wallet(self.wallet.wallet_export)
        wallet.list_invoices()
        self.paid_at = datetime.now()
        self.save()

    def __str__(self):
        return self.username
