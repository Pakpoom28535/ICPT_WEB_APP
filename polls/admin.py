from django.contrib import admin
from .models	import *
# Register your models here.
admin.site.register(StateReview)
admin.site.register(UserProfile)
admin.site.register(StateReview_User)
admin.site.register(Review_User_History)