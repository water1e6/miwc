from django.contrib import admin
from website.models import PageType, WebPage, PageCopy, PageCopyType, WebContent, WebContentSection

#class CatInLine(admin.StackedInline):
#    model = PageType
#
#class PageInLine(admin.StackedInline):
#    model = WebPage
#
#class WebPageAdmin(admin.ModelAdmin):
#    inlines = [CatInLine]
#
#class PageCatAdmin(admin.ModelAdmin):
#    inlines = [PageInLine]
#
#admin.site.register(PageCategory, PageCatAdmin)
admin.site.register(WebPage)
admin.site.register(PageType)
admin.site.register(PageCopy)
admin.site.register(PageCopyType)
admin.site.register(WebContent)
admin.site.register(WebContentSection)