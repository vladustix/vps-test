from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('uid', 'cpu', 'ram', 'hdd', 'status')

admin.site.register(Server, ServerAdmin)
