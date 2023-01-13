from django.contrib import admin
from .models import Nip05User, Relay, Payment, Wallet, Card, BackCard

class Nip05UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_key','_relays')
    
    def _relays(self, obj):
        return [x.name for x in obj.relays.all()]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('username', 'lnurl', 'paid_at')


admin.site.register(Wallet)
admin.site.register(Nip05User, Nip05UserAdmin)
admin.site.register(Relay)
admin.site.register(Card)
admin.site.register(BackCard)
admin.site.register(Payment, PaymentAdmin)
