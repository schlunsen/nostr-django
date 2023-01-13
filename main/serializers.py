from rest_framework import serializers


from .models import Nip05User, Relay, Card, BackCard

class CardSerializer(serializers.ModelSerializer):
    back_card = serializers.SerializerMethodField()
    
    def get_back_card(self, obj):
        if getattr(obj.back_card, 'image'):    
            request = self.context.get('request')
            return request.build_absolute_uri(obj.back_card.image.url)
        
    class Meta:
        model = Card
        fields = ['name', 'image', 'back_card']

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
