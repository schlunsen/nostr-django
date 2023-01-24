from rest_framework import serializers


from .models import Nip05User, Relay, Card, BackCard

class CardSerializer(serializers.ModelSerializer):
    back_card = serializers.SerializerMethodField()
    
    def get_back_card(self, obj):
        if obj.back_card and getattr(obj.back_card, 'image'):    
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.back_card.image.url)
        
    class Meta:
        model = Card
        fields = ['name', 'image', 'back_card']

class Nip05UserSerializer(serializers.ModelSerializer):
    relays = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()
    
    def get_cards(self, obj):
        return CardSerializer([x for x in obj.cards.all()], many=True).data
    
    def get_relays(self, obj):
        return RelaySerializer(obj.relays.all(), many=True).data

    class Meta:
        model = Nip05User
        fields = ['name', 'pub_key', 'relays', 'cards', 'bio', 'city', 'hook_line']


class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relay
        fields = ['name', 'url']
