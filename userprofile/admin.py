from userprofile.models import UserProfile, Facebook
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'fbid', 'vip', 'balance')
class FacebookAdmin(admin.ModelAdmin):
	list_display = ('user', 'fbid', 'name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Facebook, FacebookAdmin)
