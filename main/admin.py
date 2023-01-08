from django.contrib import admin
from .models import Nip05User, Relay

class Nip05UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_key','_relays')
    
    def _relays(self, obj):
        return [x.name for x in obj.relays.all()]

admin.site.register(Nip05User, Nip05UserAdmin)
admin.site.register(Relay)
