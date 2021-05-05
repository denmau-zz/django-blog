from django.contrib import admin
from .models import Chat, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 2  # new


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]


admin.site.register(Chat)
admin.site.register(Comment)
