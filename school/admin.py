from django.contrib import admin

from .models import Notices

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['notice_headline','published_date']

admin.site.register(Notices,NoticeAdmin)
