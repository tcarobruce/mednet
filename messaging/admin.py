from mednet.messaging.models import * 
from django.contrib.gis import admin

class VoiceMessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'phone_number', 'start_time', 'mp3_url')

class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'return_path', 'subject', 'date_sent')
    
class OutgoingMailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'to_address', 'subject', 'date_queued', 'date_sent')

class IncomingSmsMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'status','sender', 'message', 'date_sent')

class OutgoingSmsMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'message', 'date_queued', 'date_sent', 'receipt')

admin.site.register(VoiceMessage, VoiceMessageAdmin)
admin.site.register(MailMessage, MailMessageAdmin)
admin.site.register(OutgoingMailMessage, OutgoingMailMessageAdmin)
admin.site.register(OutgoingSmsMessage, OutgoingSmsMessageAdmin)
admin.site.register(IncomingSmsMessage, IncomingSmsMessageAdmin)
