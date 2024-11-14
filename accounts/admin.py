from django.contrib import admin
from .models import BaseUser,Admin,WebUser,PanelAdmin
# Register your models here.
admin.site.register(BaseUser)
admin.site.register(Admin)
admin.site.register(WebUser)
admin.site.register(PanelAdmin)