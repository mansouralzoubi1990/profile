from django.contrib import admin
from .models import *

class AboutAdminInline(admin.StackedInline):
    model = About_Paragraph

class BlogImgAdminInline(admin.StackedInline):
    model = BlogImgs

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    inlines = (AboutAdminInline,)

@admin.register(Blog)
class CVAdmin(admin.ModelAdmin):
    inlines = (BlogImgAdminInline,)


admin.site.register(Skill)
admin.site.register(Services)
admin.site.register(Achivmenet)


