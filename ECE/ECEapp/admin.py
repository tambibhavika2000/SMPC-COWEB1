from django.contrib import admin

# Register your models here.

from .models import Account,Notice,Project

# Register your models here.

admin.site.register(Account)
admin.site.register(Project)
admin.site.register(Notice)