from django.contrib import admin
from .models import Post,Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'body', 'post','created_on','active')
    list_filter=('active', 'created_on')
    search_fields=('name', 'email','body')
    actions=['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class PostAdmin(admin.ModelAdmin):
    list_display=('pk','author','title','date_posted' )
    list_filter=('author','date_posted')
    



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)