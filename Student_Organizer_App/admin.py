from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Year)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Message)
