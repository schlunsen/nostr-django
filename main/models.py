from django.db import models


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
