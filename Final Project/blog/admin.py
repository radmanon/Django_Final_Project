from django.contrib import admin
from django.db.models.base import Model

from blog.models import Comment, Post
from django.utils.safestring import mark_safe
# Register your models here.



class PostInLine(admin.TabularInline):
    model = Post
    extra = 0

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="{obj.title}" width="100" height="100">'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
    )
    show_image.short_description = "نمایش عکس"


    list_display = ["get_image", "title", "author", "status", "category", "updated_at", "created_at"]
    list_filter = ("status", "category", "author", "created_at")
    search_fields = ("title", "short_description", "long_description")
    ordering = ("created_at",)
    list_editable = ("title", "status", "category")
    inlines = [CommentInLine]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "status", "created_at"]
    list_filter = ("status", "created_at")
    search_fields = ("last_name", "first_name", "title")
    ordering = ("created_at",)
    sortable_by = ("first_name", "last_name", "membership_at")
    list_editable = ("status",)
    #readonly_fields = ('post', 'user', "text")