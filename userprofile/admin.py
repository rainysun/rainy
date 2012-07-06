from userprofile.models import UserProfile, Facebook, Sina
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'fbid', 'vip', 'balance')
class FacebookAdmin(admin.ModelAdmin):
	list_display = ('user', 'fbid', 'name', 'email')
class SinaAdmin(admin.ModelAdmin):
	list_display = ('user', 'said', 'name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Facebook, FacebookAdmin)
admin.site.register(Sina, SinaAdmin)
