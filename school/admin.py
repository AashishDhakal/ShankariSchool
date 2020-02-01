from django.contrib import admin

from .models import Notices,CEOMessage,Testimonials,AboutSection,ImportantNotice,Downloads,Gallery

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['notice_headline','published_date']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['testimonial_author','testimonial_designation']

admin.site.register(Notices,NoticeAdmin)
admin.site.register(CEOMessage)
admin.site.register(AboutSection)
admin.site.register(ImportantNotice)
admin.site.register(Downloads)
admin.site.register(Gallery)
admin.site.register(Testimonials,TestimonialAdmin)
