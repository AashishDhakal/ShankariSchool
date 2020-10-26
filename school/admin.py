from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['notice_headline','published_date']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['testimonial_author','testimonial_designation']

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name','designation']

class ParentInformationAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = ['grade','student_name','parent_name','parent_email','parent_phone']
    list_filter = ['grade']
    search_fields = ['student_name',]
    actions = ['export_as_csv']

admin.site.register(Notices,NoticeAdmin)
admin.site.register(CEOMessage)
admin.site.register(AboutSection)
admin.site.register(ImportantNotice)
admin.site.register(Downloads)
admin.site.register(Gallery)
admin.site.register(HomePage)

admin.site.register(TeamMember,TeamMemberAdmin)
admin.site.register(Testimonials,TestimonialAdmin)
admin.site.register(ParentInformation,ParentInformationAdmin)
