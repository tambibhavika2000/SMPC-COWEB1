from django.contrib import admin

# Register your models here.

from .models import Notice,Project,Faculty,People,Company,Event

# Register your models here.
admin.site.site_header='ECE ADMIN PANEL'
admin.site.site_title='SVNIT-ECE'

admin.site.register(Project)
admin.site.register(Notice)
admin.site.register(Faculty)
admin.site.register(People)
admin.site.register(Company)
admin.site.register(Event)