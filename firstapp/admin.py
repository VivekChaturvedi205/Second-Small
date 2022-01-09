from django.contrib import admin
from firstapp.models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display=['Customer_Name','Image']
admin.site.register(Upload,UploadAdmin)

