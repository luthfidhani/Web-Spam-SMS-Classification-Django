from django.contrib import admin

from .models import Data

class SmsAdmin(admin.ModelAdmin):
    list_display = ('id','text', 'prediction', 'created_at')

admin.site.register(Data, SmsAdmin)


