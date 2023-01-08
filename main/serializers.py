from rest_framework import serializers


from .models import Nip05User, Relay


class Nip05UserSerializer(serializers.ModelSerializer):
    relays = serializers.SerializerMethodField()

    def get_relays(self, obj):
        return RelaySerializer(obj.relays.all(), many=True).data

    class Meta:
        model = Nip05User
        fields = ['name', 'pub_key', 'relays']


class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relay
        fields = ['name', 'url']
