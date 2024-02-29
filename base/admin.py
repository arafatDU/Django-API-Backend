from django.contrib import admin
from .models import Advocates

class AdvocatesAdmin(admin.ModelAdmin):
  list_display = ["username", "bio"]
  
# Register your models here.
admin.site.register(Advocates, AdvocatesAdmin)