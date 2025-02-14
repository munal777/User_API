from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)   #customizing the user interface of profile model by showing its id


admin.site.register(Profile, ProfileAdmin)