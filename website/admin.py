from django.contrib import admin
from website.models import PageCategory, WebPage

class CatInLine(admin.StackedInline):
    model = PageCategory

class PageInLine(admin.StackedInline):
    model = WebPage

class WebPageAdmin(admin.ModelAdmin):
    inlines = [CatInLine]

class PageCatAdmin(admin.ModelAdmin):
    inlines = [PageInLine]

admin.site.register(PageCategory, PageCatAdmin)
admin.site.register(WebPage)