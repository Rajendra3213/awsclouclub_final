from django.contrib import admin
from .models import EventSystem,GrandEventSystem,GuestSpeaker,EventParticipant,MerchantSponsers,GrandEventSession,GrandEventParticipant
from unfold.admin import ModelAdmin

@admin.register(EventSystem)
class AdminEventSytem(ModelAdmin):
    list_display = ('title', 'startDate', 'endDate','EventStatus')
    list_filter = ('EventStatus',)
@admin.register(EventParticipant)
class EventParticipantAdmin(ModelAdmin):
    list_display = ('account_suscriber', 'event_suscribed', 'participant_suscriber')
    list_filter = ('account_suscriber__email', 'event_suscribed', 'participant_suscriber')
    search_fields=('account_suscriber__email', 'event_suscribed__title', 'participant_suscriber')

@admin.register(GrandEventSystem)
class AdminGrandEventSytem(ModelAdmin):
    list_display = ('title', 'startDate', 'endDate','EventStatus')
    list_filter = ('EventStatus',)

@admin.register(GuestSpeaker)
class AdminGuestSpeaker(ModelAdmin):
    list_display = ('SpeakerName', 'SpeakerTitle', 'event_titles')

    def event_titles(self,obj):
        return ', '.join([event.title for event in obj.events.all()])
    event_titles.short_description = 'Event Titles'


@admin.register(MerchantSponsers)
class MerchantSponsersAdmin(ModelAdmin):
    list_display=('merchant_name','merchant_logo','merchant_desc')
    search_fields=('merchant_name',)

@admin.register(GrandEventSession)
class GrandEventSessionAdmin(ModelAdmin):
    list_display = ('title', 'startTime', 'endTime')
    search_fields = ('title', 'sessions__title')

@admin.register(GrandEventParticipant)
class GrandEventParticipantAdmin(ModelAdmin):
    list_display = ('account_suscriber', 'event_suscribed', 'participant_suscriber')
    list_filter = ('account_suscriber__email', 'event_suscribed', 'participant_suscriber')
    search_fields=('account_suscriber__email', 'event_suscribed__title', 'participant_suscriber')