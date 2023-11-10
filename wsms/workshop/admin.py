from django.contrib import admin
from .models import *
fname='first_name'
class UsersAdmin(admin.ModelAdmin):
    search_fields=['id','first_name','last_name','user_type']
    list_display=['first_name','last_name','user_name','user_type','is_active']
    # list_display_links = ('id')
    list_editable=['last_name','user_type']
    list_filter=['user_type']

class ItemsAdmin(admin.ModelAdmin):
    list_display=['id','Serial_no','status','is_valid','is_accepted']
    list_editable=['is_valid','is_accepted','status']
    
    list_filter=['is_valid','status']
# Register your models here.
admin.site.register(User,UsersAdmin)
admin.site.register(Item,ItemsAdmin)
admin.site.register(Assignments)
admin.site.register(Section)
admin.site.register(Component)
admin.site.register(Notification)
