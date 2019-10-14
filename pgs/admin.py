from django.contrib import admin
from . models import Pgs, Area, Gender


class PgsAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'category')


admin.site.register(Pgs, PgsAdmin)
admin.site.register(Area)
admin.site.register(Gender)