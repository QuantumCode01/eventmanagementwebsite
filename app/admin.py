from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(event)
class EventAdmin(admin.ModelAdmin):
      list_display=('id','name','event_name','date','time','location','image','is_liked','liked_users')
  
#   this liked_user funtion make sure that username of user who liked the event, is visible on admin panel under the heading of liked By Users
      def liked_users(self, obj):
            return ", ".join([user.username for user in obj.liked_by_users.all()])
    
      liked_users.short_description = 'Liked By Users'