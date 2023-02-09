from django.contrib import admin
from django.contrib.auth.models import User, Group
from web.models import FamilyTree

admin.site.unregister(User)
admin.site.unregister(Group)


class FamilyTreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')

admin.site.register(FamilyTree, FamilyTreeAdmin)
